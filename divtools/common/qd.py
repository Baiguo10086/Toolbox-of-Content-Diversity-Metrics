from abc import ABC, abstractmethod
from typing import List
import random


class Individual(ABC):
    @abstractmethod
    def qd_score(self):
        pass



class Population(ABC):

    def __init__(self, individual, size):
        """
        初始化种群。
        :param individual: 个体构造函数。
        :param size
        """
        self.size = size
        if issubclass(individual, Individual):
            self.individuals = [individual() for _ in range(self.size)]
        else:
            raise ValueError("Class does not implement the Individual interface")

    @abstractmethod
    def evaluate(self, individual):
        pass

    @abstractmethod
    def mutate(self, individual):
        pass

    @abstractmethod
    def select(self):
        pass


class DefaultIndividual(Individual):
    attributes: List
    fitness: int

    def __init__(self, attributes=None):
        if attributes is None:
            attributes = [random.random() for _ in range(10)]
        self.attributes = attributes
        self.fitness = 0

    def qd_score(self):
        return sum(self.attributes)


class DefaultPopulation(Population):

    def evaluate(self, individual):
        individual.fitness = individual.qd_score()
        return individual.fitness

    def mutate(self, individual):
        mutated_attributes = [attr + random.uniform(-0.1, 0.1) for attr in individual.attributes]
        return DefaultIndividual(mutated_attributes)

    def select(self):
        self.individuals.sort(key=lambda ind: ind.fitness, reverse=True)
        return self.individuals[:len(self.size) // 2]


class QD:
    population: Population

    def __init__(
            self,
            population=None,
            population_size=100
    ):
        self.population = population or DefaultPopulation(DefaultIndividual, population_size)
        self.population_size = population_size

    def evolve(self, generations):
        for _ in range(generations):
            # 选择阶段
            selected_individuals = self.population.select()

            # 变异阶段
            mutated_individuals = [self.population.mutate(ind) for ind in selected_individuals]

            # 评估阶段
            for ind in mutated_individuals:
                self.population.evaluate(ind)

            # 更新种群（这里的策略可以根据需要进行修改）
            self.population.individuals = mutated_individuals + self.population.individuals
            self.population.individuals = sorted(self.population.individuals, key=lambda ind: ind.fitness,
                                                 reverse=True)[:self.population_size]

    def get_elites(self, elites_size):
        """
        获取精英个体。
        """
        # 实现获取精英个体的逻辑
        return sorted(self.population.individuals, key=lambda ind: ind.fitness, reverse=True)[:elites_size]

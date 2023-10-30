
import numpy as np
from typing import List


def calculate_linear_regression_least_squares(x_list:List[float],y_list:List[float]) -> float:
    X = np.array(x_list)
    Y = np.array(y_list)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sum((X - mean_X) ** 2)
    slope = numerator / denominator
    intercept = mean_Y - slope * mean_X

    predicted_Y = slope * X + intercept
    residuals = Y - predicted_Y
    
    mse = np.mean(residuals**2)
    return mse

def calculate_average_vertical_distance(x_list:List[float],y_list:List[float]) -> float:
    X = np.array(x_list)
    Y = np.array(y_list)
    
    coe = (Y[-1]- Y[0])/(X[-1]-X[0])
    intercept = Y[0]
    
    predicted_Y = coe * X +intercept
    residuals = Y - predicted_Y
    
    average=np.mean(abs(residuals))
    return average
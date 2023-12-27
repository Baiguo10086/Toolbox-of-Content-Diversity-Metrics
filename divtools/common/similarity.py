def get_similar_rows(training_data):
    similar_rows = set()
    for train_segment in training_data:
        for row in train_segment:
            similar_rows.add(tuple(row))
    return similar_rows


def get_similar_cols(training_data):
    similar_cols = set()
    for train_segment in training_data:
        train_segment = [list(row) for row in zip(*train_segment)]
        for row in train_segment:
            similar_cols.add(tuple(row))
    return similar_cols


def similarity_optimized(segment, similar_rows, similar_cols):
    similarity = 0
    for row in segment:
        # Convert the row to a tuple for consistency
        row_tuple = tuple(row)
        # Check if the row appears in the preprocessed training data
        if row_tuple in similar_rows:
            similarity += 1

    segment = [list(row) for row in zip(*segment)]

    for col in segment:
        col_tuple = tuple(col)
        if col_tuple in similar_cols:
            similarity += 1

    return similarity

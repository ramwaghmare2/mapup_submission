import pandas as pd
import numpy as np
from import_data import dataset_1, dataset_2
data = dataset_1
data2 = dataset_2

def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    for i in range(min(df.shape)):
        df.iloc[i, i] = 0
    
    return df
#result = generate_car_matrix(data)
#result

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(np.select(conditions, choices), index=df.index)
    
    type_counts = df['car_type'].value_counts().to_dict()
    
    type_counts = dict(sorted(type_counts.items()))
    
    return type_counts

#result = get_type_count(data)
#result



def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    mean_bus = df['bus'].mean()
    
    indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    
    indexes.sort()
    
    return indexes
#result = get_bus_indexes(data)
#result

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    route_avg_truck = df.groupby('route')['truck'].mean()
    
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    
    filtered_routes.sort()
    
    return filtered_routes
#result = filter_routes(data)
#result

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    
    matrix = matrix.round(1)
    
    return matrix
#result = multiply_matrix(data)
#result


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    df['start_time'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%A %H:%M:%S')
    
    df['end_time'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], format='%A %H:%M:%S')
    
    df['time_diff'] = df['end_time'] - df['start_time']
    time_check = (df['time_diff'] != pd.Timedelta(days=1)) | (df['start_time'].dt.dayofweek != 0) | (df['end_time'].dt.dayofweek != 6)
    
    completeness_series = df.groupby(['id', 'id_2'])['time_diff'].apply(lambda x: x.any()).reindex(df[['id', 'id_2']].drop_duplicates().itertuples(index=False)).fillna(False)
    
    return completeness_series

# data = data2 
# result_matrix = time_check(data)
# result_matrix

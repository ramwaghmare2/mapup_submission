import pandas as pd
from import_data import dataset_3
data = dataset_3


def calculate_distance_matrix(df)->pd.DataFrame():
    locations = sorted(set(data['id_start']).union(set(data['id_end'])))

    distances = pd.DataFrame(index=locations, columns=locations)
    distances = distances.fillna(0)  # Fill NaN values with 0
    
    for _, row in data.iterrows():
        start = row['id_start']
        end = row['id_end']
        distance = row['distance']
        
        distances.at[start, end] += distance
        distances.at[end, start] += distance
    
    return distances

# data = data 
# result = calculate_distance_matrix(data)
# result

def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df


import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Function to load data from file
    data = pd.read_csv(file_path)
    return data

def explore_basic_stats(data):
    # Function to explore basic statistics of the dataset
    stats = data.describe()
    return stats

def visualize_distribution(data, column):
    # Function to visualize distribution of a specific column
    plt.hist(data[column])
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title('Distribution of ' + column)
    plt.show()

import pandas as pd
import numpy as np


def convert_to_list(folder_name):
    filtered_df = pd.read_csv(folder_name + "/filteredanalysis.csv", usecols=lambda column: column != 'Category')
    ocean_traits_df = pd.read_csv(folder_name + "/ocean_traits.csv", skiprows=1, header=None)
    filtered_values = filtered_df['Value'].values.tolist()
    ocean_traits_values = ocean_traits_df.values.flatten().tolist()
    return filtered_values, ocean_traits_values



filtered_2d_list = []
ocean_2d_list = []

for i in range(1, 47):
    folder_name = "sample" + str(i)
    filtered_values, ocean_traits_values = convert_to_list(folder_name)
    filtered_2d_list.append(filtered_values)
    ocean_2d_list.append(ocean_traits_values)


correlations = np.corrcoef(np.array(filtered_2d_list).T, np.array(ocean_2d_list).T)
num_filtered_lists = len(filtered_2d_list[0])
num_ocean_lists = len(ocean_2d_list[0])
correlation_matrix = pd.DataFrame(correlations[:num_filtered_lists, num_filtered_lists:], index=range(1, num_filtered_lists + 1), columns=range(1, num_ocean_lists + 1))



feature_names = ["affection", "body", "children", "cold", "communication", "family", "friends", "giving", "hearing", "listen", "love", "movement", "music", "negative_emotion", "nervousness", "night", "optimism", "pain", "party", "positive_emotion", "shame", "speaking", "vacation", "violence", "youth"]
ocean_traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]


correlation_matrix.index = feature_names
correlation_matrix.columns = ocean_traits
correlation_matrix.to_csv('correlation_matrix.csv')


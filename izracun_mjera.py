import networkx as nx
import pandas as pd

def read_csv_edges(file_path):
    df = pd.read_csv(file_path)
    G = nx.from_pandas_edgelist(df, 'Source', 'Target', ['Weight'])
    return G

file_path_1 = 'fidit.csv'  # Replace with the path to your first .edges file
file_path_2 = 'foi.csv'  # Replace with the path to your second .edges file

# Read the two .edges files and create the graphs
G2 = read_csv_edges(file_path_1)
G1 = read_csv_edges(file_path_2)

# Perform analysis on the first graph (G1)
# Global measures
global_measures_G1 = {
    'Number of Nodes': nx.number_of_nodes(G1),
    'Number of Edges': nx.number_of_edges(G1),
    'Average Node Degree': nx.average_degree_connectivity(G1),
    # Add other global measures for G1
}

# Central measures
central_measures_G1 = {
    'Degree Centrality': nx.degree_centrality(G1),
    'Betweenness Centrality': nx.betweenness_centrality(G1),
    # Add other central measures for G1
}

# Local measures
local_measures_G1 = {
    'Closeness Centrality': nx.closeness_centrality(G1),
    'Eigenvector Centrality': nx.eigenvector_centrality(G1),
    # Add other local measures for G1
}

# Display analysis for G1
global_df_G1 = pd.DataFrame.from_dict(global_measures_G1, orient='index', columns=['Value'])
print("Global Network Measures for G1(FOI):")
print(global_df_G1)

central_df_G1 = pd.DataFrame.from_dict(central_measures_G1)
print("\nCentral Network Measures for G1(FOI):")
print(central_df_G1.head(10))  # Display the top 10 nodes sorted by measure

local_df_G1 = pd.DataFrame.from_dict(local_measures_G1)
print("\nLocal Network Measures for G1(FOI):")
print(local_df_G1.head(10))  # Display the top 10 nodes sorted by measure


global_measures_G2 = {
    'Number of Nodes': nx.number_of_nodes(G2),
    'Number of Edges': nx.number_of_edges(G2),
    'Average Node Degree': nx.average_degree_connectivity(G2),
    # Add other global measures for G2
}

# Central measures
central_measures_G2 = {
    'Degree Centrality': nx.degree_centrality(G2),
    'Betweenness Centrality': nx.betweenness_centrality(G2),
    # Add other central measures for G2
}

# Local measures
local_measures_G2 = {
    'Closeness Centrality': nx.closeness_centrality(G2),
    'Eigenvector Centrality': nx.eigenvector_centrality(G2),
    # Add other local measures for G2
}

# Display analysis for G2
global_df_G2 = pd.DataFrame.from_dict(global_measures_G2, orient='index', columns=['Value'])
print("Global Network Measures for G2(FIDIT):")
print(global_df_G2)

central_df_G2 = pd.DataFrame.from_dict(central_measures_G2)
print("\nCentral Network Measures for G2(FIDIT):")
print(central_df_G2.head(10))  # Display the top 10 nodes sorted by measure

local_df_G2 = pd.DataFrame.from_dict(local_measures_G2)
print("\nLocal Network Measures for G2(FIDIT):")
print(local_df_G2.head(10))  # Display the top 10 nodes sorted by measure

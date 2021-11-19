import itertools
import networkx as nx
import time
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
import networkx.algorithms.community as nx_comm
import numpy as np
from sklearn.cluster import SpectralClustering

print("STATISTICS:")
print()
print("karate club")
k1 = nx.read_gml("karate.gml", label='id')
print(nx.info(k1))
avg = nx.average_clustering(k1)
print("Average clustering coefficient : ", avg)
print("Average path length: ", nx.average_shortest_path_length(k1))
print("---------------------------------------------------------------------------------------------------")
print()

print("Dolphin club")
k2 = nx.read_gml("dolphins.gml")
print(nx.info(k2))
avg = nx.average_clustering(k2)
print("Average clustering coefficient : ", avg)
print("Average path length : ", nx.average_shortest_path_length(k2))
print("---------------------------------------------------------------------------------------------------")


print("Jazz Club")
f = open("jazz.net","r")
# read into list lines
l = f.readlines()
f.close()
nf = open("jazz.net","w")
for i in l:
    if i != l[0] and i != l[1] and i != l[2]:
        nf.write(i)
nf.close()
j = nx.read_weighted_edgelist("jazz.net")
print(nx.info(j))
print("Average path length : ", nx.average_shortest_path_length(j))
avg = nx.average_clustering(j)
print("Average clustering coefficient : ", avg)
print("--------------------------------------------------------------------------------------------------")

import itertools
import networkx as nx
import time
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
import networkx.algorithms.community as nx_comm
import numpy as np
from sklearn.cluster import SpectralClustering


#reading graphs
k1 = nx.read_gml('karate.gml', label = 'id')
k2 = nx.read_gml('dolphins.gml')
k3 = nx.read_weighted_edgelist('jazz.net')
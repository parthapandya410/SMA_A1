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



#Girvan-Newman algorithm
k1 = nx.read_gml('karate.gml', label = 'id')
k2 = nx.read_gml('dolphins.gml')
k3 = nx.read_weighted_edgelist('jazz.net')

print("GIRVAN-NEWMAN ALGORITHM")
print()
print("karate club network : ")
k1 = nx.read_gml("karate.gml",label ='id')
k = 10
old = time.time()
comp = girvan_newman(k1)
for communities in itertools.islice(comp, k):
    print(tuple(sorted(c) for c in communities))
new = time.time()
print()  
print("Number of clusters",len(communities))   
print("Modularity of karate club:")
print(nx_comm.modularity(k1, communities))
print("Time taken : ", new - old)
print("------------------------------------------------------------------------------------------------------------")
print()
print("jazz network : ")
k2 = nx.read_weighted_edgelist("jazz.net")
old = time.time()
comp = girvan_newman(k2)
for communities in itertools.islice(comp, k):
    print(tuple(sorted(c) for c in communities))
new = time.time()
print()
print("Modularity of jazz club:")
print(nx_comm.modularity(k2, communities))     
print("Number of clusters",len(communities))   #no_of_clusters
print("Time taken : ", new - old)
print("-------------------------------------------------------------------------------------------------------------")
print()
print("dolphins network - gievan newman clustering : ")
k3 = nx.read_gml("dolphins.gml")
old = time.time()
comp = girvan_newman(k3)
for communities in itertools.islice(comp, k):
    print(tuple(sorted(c) for c in communities))
new = time.time()
print()
print("Modularity of dolphins club:")
print(nx_comm.modularity(k3, communities))  
print("Number of clusters: ",len(communities))  
print("Time taken : ", new - old)
print("-------------------------------------------------------------------------------------------------------------")





#modularity-based clustering 
k1 = nx.read_gml('karate.gml', label = 'id')
k2 = nx.read_gml('dolphins.gml')
k3 = nx.read_weighted_edgelist('jazz.net')

print("MODULARITY BASED CLUSTERING")
#m1 = nx.read_weighted_edgelist("karate.gml")
print()
print("Karate Club : ")
old = time.time()
n_list = list(greedy_modularity_communities(k1))
new = time.time()
for n in n_list:
    print(sorted(n))
print("# clusters formed:"+str(len(n_list))) 
print("Modularity of karate club:")
ng = (list(sorted(n) for n in n_list))
print(nx_comm.modularity(k1, ng))
print("Time taken:"+str(new-old))
print("--------------------------------------------------------------------------------------------------------")
print()
print("Jazz Club : ")
#m2 = nx.read_weighted_edgelist("jazz.net")
old = time.time()
n_list = list(greedy_modularity_communities(k2))
new = time.time()
for n in n_list:
    print(sorted(n))
print("# clusters formed:"+str(len(n_list)))  
print("Modularity of jazz club:")
ng = (list(sorted(n) for n in n_list))
print(nx_comm.modularity(k2, ng))
print("Time taken:"+str(new-old))
print("--------------------------------------------------------------------------------------------------------")

print()
print("Dolphins Club : ")
old = time.time()
#m3 =  nx.read_weighted_edgelist("dolphins.net")
old = time.time()
n_list = list(greedy_modularity_communities(k3))
new = time.time()
for n in n_list:
    print(sorted(n))
print("# clusters formed:"+str(len(n_list)))  
print("Modularity of dolphin club:")
ng = (list(sorted(n) for n in n_list))
print("Time taken:"+str(new-old))
print(nx_comm.modularity(k3, ng))
print("--------------------------------------------------------------------------------------------------------")




print("SPECTRAL CLUSTERING")
print()
k1 = nx.read_gml('karate.gml', label = 'id')
k2 = nx.read_gml('dolphins.gml')
k3 = nx.read_weighted_edgelist('jazz.net')

print("Karate Club :")
print()
# Graph1
old = time.time()
a1 = nx.to_numpy_matrix(k1)
sc = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities 
sc.fit(a1)

new = time.time()


# find the nodes of the communities
labels = sc.labels_

ls = [[] for i in range(4)]

i = 1
for x in labels:
    if(x == 0):
        ls[0].append(i)
        i += 1
    elif(x == 1):
        ls[1].append(i)
        i += 1
    elif(x == 2):
        ls[2].append(i)
        i += 1
    elif(x == 3):
        ls[3].append(i)
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters Found : ")
print(len(ls)) 
print("Modularity Score: " + str(nx_comm.modularity(k1, ls)))
print("Time taken : ", new - old)
print("---------------------------------------------------------------------------------------------------------------")


# Graph2
print("DOLPHIN CLUB")
oldtime = time.time()
a2 = nx.to_numpy_matrix(k2)

#  graph to a list
lsg2 = list(k2)
sc = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)
# find communities 
sc.fit(a2)

newtime = time.time()
# find the nodes of the communities
labels = sc.labels_
ls = [[] for i in range(4)]
i = 0
for x in labels:
    if(x == 0):
        ls[0].append(lsg2[i])
        i += 1
    elif(x == 1):
        ls[1].append(lsg2[i])
        i += 1
    elif(x == 2):
        ls[2].append(lsg2[i])
        i += 1
    elif(x == 3):
        ls[3].append(lsg2[i])
        i += 1
print("Clusters : ")
print(ls)
print("Number of Clusters Found : ")
print(len(ls)) 
print("Modularity Score : " + str(nx_comm.modularity(k2, ls)))
print("Runtime : ", new - old)
print("---------------------------------------------------------------------------------------------------------------")


print("Jazz club")
old = time.time()
a3= nx.to_numpy_matrix(k3)



sc = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities 
sc.fit(a3)

newtime = time.time()


# find the nodes of the communities
labels = sc.labels_

ls = [[] for i in range(4)]

i = 1
for x in labels:
    if(x == 0):
        ls[0].append(str(i))
        i += 1
    elif(x == 1):
        ls[1].append(str(i))
        i += 1
    elif(x == 2):
        ls[2].append(str(i))
        i += 1
    elif(x == 3):
        ls[3].append(str(i))
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters : ")
print(len(ls)) 
print("Modularity Score : " + str(nx_comm.modularity(k3, ls)))
print("Runtime : ", new - old)
print("--------------------------------------------------------------------------------------------------------")


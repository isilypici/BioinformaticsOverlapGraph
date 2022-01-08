import networkx as nx
import matplotlib.pyplot as plt
import random

def compare(kmer1,kmer2, G):
    
    suffix = kmer1[1:]
    prefix = kmer2[:-1]
    
    print("\t\tsuffix:", suffix, "prefix:", prefix)
    
    if(prefix == suffix):
        print("\t\t\t\t\t\t\t\t\t+")
        G.add_edge(kmer1,kmer2,weight = len(suffix))
        
    return G

def reconstruct(G):
    nodes = list(G)
    edges = list(G.edges)
    newGenome = []
    #print(len(nodes))
    #print(len(edges))
    choosenNode = -1
    counter = 0
    while counter < len(nodes):
        if (choosenNode != -1):
            randomStartNode = nodes.index(choosenNode)
        else:
            randomStartNode = random.randint(0,len(nodes)-1)
        
        #biggestEdge = random.randint(0,len(edges[randomStartNode])-1)
        print(randomStartNode, " ", edges[randomStartNode], " >> ", edges[randomStartNode][1])
        choosenNode = edges[randomStartNode][1]
        print(nodes.index(choosenNode) , " noduna geçildi...")
        
        newGenome.append(choosenNode)
        print(newGenome)
        
        counter += 1
        



genomes = ["gtacgt","tacgta","acgtac","cgtacg","gtacga","tacgat"]
temp = genomes.copy()
G = nx.DiGraph()

while len(temp)>0:
    kmer1 = temp[0]
    print("işlenen:",kmer1)
    
    j = 0
    while j<len(genomes):
        kmer2 = genomes[j]
        if(kmer1 == kmer2):
            j+=1
            continue
        else:
            print("\t",kmer1,"-->",kmer2)
            compare(kmer1 ,kmer2 , G)
            j+=1
    
    
    temp.pop(0)
    
reconstruct(G)

#output = nx.shortest_path(compare("tgtgtc","gtgtca"), weight='weight')

subax1 = plt.subplot(121)
nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')

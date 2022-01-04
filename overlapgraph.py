import networkx as nx

def compare(kmer1,kmer2):
    
    G = nx.Graph()
    
    suffix = kmer1[1:]
    prefix = kmer2[:-1]
    
    print("prefix:", prefix, "suffix:", suffix)
    
    if(prefix == suffix):
        G.add_edge(kmer1,kmer2,weight = len(suffix))
        
    return G

compare("tgtgtc","gtgtca")


output = nx.shortest_path(compare("tgtgtc","gtgtca"), weight='weight')

print(output)
import networkx as nx
import matplotlib.pyplot as plt #grafiği görsel olarak da göstermek için 
import random #TODO kaldırılabilir belli değil

def getSimilarity(read1,read2,threshold=4): 
    """
    read1, main read to be compared
    read2 other read to be compared
    returns same bases count suffix of read1 and prefix o read2
    """
    for i in range(len(read1)):
        if(len(read1)-i < threshold):
            return 0
        isSame = read1[i:] == read2[:len(read2)-i] 
        if(isSame):
            return len(read1)-i
    return 0
        
    
def reconstruct(G):
    nodes = list(G) #listede nodları tuttuk
    edges = list(G.edges) #listede edgeleri tuttuk 0. gelen 1. gittiği nod
    newGenome = [] 
    #print(len(nodes))
    #print(len(edges))
    choosenNode = -1 #rastgele sayı önemsiz
    counter = 0
    while counter < len(nodes): #bütün nodları gezerse gezdikten sonra devam etmesine gerek yok
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

G = nx.DiGraph()
G.add_nodes_from(genomes)



for _read1 in range(len(genomes)):
    read1 = genomes[_read1]
    rest = genomes.copy()
    rest.remove(read1)
    
    for read2 in rest:
        sim = getSimilarity(read1,read2)
        if(sim>0):
            print(sim ," ", read1," -> ",read2)
            G.add_weighted_edges_from([(read1,read2,sim)])
        
        
"""

temp = genomes.copy()

while len(temp)>0:
    kmer1 = temp[0]
#    print("işlenen:",kmer1)
    
    j = 0
    while j<len(genomes):
        kmer2 = genomes[j]
        if(kmer1 == kmer2): #kendi kendini kontrol etmesin diye kendisini geçiyoruz 
            j+=1
            continue
        else:
#            print("\t",kmer1,"-->",kmer2) #diğer tüm kmer gnomeları karşılaştırarak node ve edge oluşturuyoruz
            getSimilarity(kmer1 ,kmer2)
            j+=1
    
    
    temp.pop(0) #işlenmiş elemanı çıkartıyoruz 
"""
#reconstruct(G)

#output = nx.shortest_path(compare("tgtgtc","gtgtca"), weight='weight') #2 nod araasında en kısa yolu bulmak için bir fonksiyon (kullanılmadı)

#subax1 = plt.subplot(121)

nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G))














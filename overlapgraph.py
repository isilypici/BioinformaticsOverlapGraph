import networkx as nx
import matplotlib.pyplot as plt #grafiği görsel olarak da göstermek için 
import random #TODO kaldırılabilir belli değil

def compare(kmer1,kmer2, G): 
    
    #difference = #difference büyüdükçe benzerlik azalacak 
    suffix = kmer1[1:]
    prefix = kmer2[:-1] 
    #TODO kaç adet suffix prefix eşleşmesi varsa o weight olmalı weight de bu sayı olmalı
    #o kadar sayı kadar geriden başlamalı
    
    if(prefix == suffix):
        print("\t\tsuffix:", suffix, "prefix:", prefix , " + ")
        G.add_edge(kmer1,kmer2,weight = len(suffix)) 
        #TODO weight ayarlanmalı
    else:
        print("\t\tsuffix:", suffix, "prefix:", prefix)
    return G

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
temp = genomes.copy()
G = nx.DiGraph()

while len(temp)>0:
    kmer1 = temp[0]
    print("işlenen:",kmer1)
    
    j = 0
    while j<len(genomes):
        kmer2 = genomes[j]
        if(kmer1 == kmer2): #kendi kendini kontrol etmesin diye kendisini geçiyoruz 
            j+=1
            continue
        else:
            print("\t",kmer1,"-->",kmer2) #diğer tüm kmer gnomeları karşılaştırarak node ve edge oluşturuyoruz
            compare(kmer1 ,kmer2 , G)
            j+=1
    
    
    temp.pop(0) #işlenmiş elemanı çıkartıyoruz 
    
reconstruct(G)

#output = nx.shortest_path(compare("tgtgtc","gtgtca"), weight='weight') #2 nod araasında en kısa yolu bulmak için bir fonksiyon (kullanılmadı)

#subax1 = plt.subplot(121)

nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')

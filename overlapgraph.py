import networkx as nx
import matplotlib.pyplot as plt #grafiği görsel olarak da göstermek için 
import random #TODO kaldırılabilir belli değil
import time

def getSimilarity(read1,read2,threshold=40): 
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
        

class GenomeProject:
    def __init__(self,genomeArray):
        self.reads = genomeArray
        
        self.startingNode = genomeArray[0]#first node is starting node
        self.traveledNodes = [self.startingNode]
        
        
        self.G = nx.DiGraph()#initilize graph
        self.G.add_nodes_from(self.reads)#add nodes from array
        
        
        self.drawGraph()
        self.assembleGenome()
        
        
    def drawGraph(self):
        for _read1 in range(len(self.reads)):
            read1 = self.reads[_read1]
            rest = self.reads.copy()
            rest.remove(read1)
        
            for read2 in rest:
                sim = getSimilarity(read1,read2)
                if(sim>0):
                    self.G.add_weighted_edges_from([(read1,read2,sim)])
                    
                    
    def assembleGenome(self):
        self.path = [self.startingNode]
        
        self.traversal(self.startingNode)
        self.concatenate()
            
    def traversal(self,read):
        nodeNames = []
        weights = []
        for i in [i for i in list(self.G.adjacency()) if i[0] == read ]:
            for nodeName,val in i[1].items():
                if(nodeName in self.traveledNodes):
                    continue
                nodeNames.append(nodeName)
                for _w,weight in val.items():
                    weights.append(weight)

        allList = list(zip(nodeNames,weights))
        
        mostWeight = 0
        mostWeightNode = None
        
        for edges in allList:
            
            if(edges[1] > mostWeight):
                mostWeightNode = edges[0]
                mostWeight = edges[1]
        
        if(mostWeightNode == None):
            return
        
        self.traveledNodes.append(mostWeightNode)
        self.path.append(mostWeightNode)
        self.traversal(mostWeightNode)

    def concatenate(self):
        self.gene = self.startingNode
        for i in self.path[1:]:
            self.gene += i[-1]
            

class geneSep:
    def __init__(self,kmer,length=None):
        self.kmer = kmer
        self.reads = []
        with open("gene.fna") as f:
            lines = f.readlines()
            for i in lines.copy():
                if(">" in i):
                    lines.remove(i)
            
            self.text = "".join(lines).replace("\n","")
            if(length != None):
                self.text = self.text[0:length]
            
        self.createReads()
        
    def createReads(self):
        for i in range(len(self.text)-self.kmer):
            self.reads.append(self.text[i:i+self.kmer])
        print("len of reads:",len(self.reads))
    def isTextSame(self,txt):
        if(self.text == txt):
            return True
        else:
            return False
            

#readList = ["gtacgt","tacgta","acgtac","cgtacg","gtacga","tacgat"]
#GenomeProject(readList)

#for i in range(300,30000,500):
    
start = time.time()

rd = geneSep(50)
print("gene sep")

gp = GenomeProject(rd.reads)
print("genome project")

print(rd.isTextSame(gp.gene))
print("check txt")
   
end = time.time()
print(end - start)



#reconstruct









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

#nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
#nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G))














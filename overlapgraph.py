import networkx as nx
import matplotlib.pyplot as plt #grafiği görsel olarak da göstermek için 
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
        for i in range(len(self.text)-self.kmer+1):
            self.reads.append(self.text[i:i+self.kmer])
    def isTextSame(self,txt):
        if(self.text == txt):
            return True
        else:
            return False
            

#readList = ["gtacgt","tacgta","acgtac","cgtacg","gtacga","tacgat"]
#GenomeProject(readList)

times = []
for i in range(300,2000,50):
    start = time.time()
    
    rd = geneSep(50,i)
    
    gp = GenomeProject(rd.reads)
    
    print(rd.isTextSame(gp.gene))
       
    end = time.time()
    print(i, end - start)
    times.append(end-start)

x = range(300,2000,50)

plt.plot(x,times)
plt.show()














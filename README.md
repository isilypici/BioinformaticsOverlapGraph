# Bioinformatics Overlap Layout Graph Implementation

### work in progress ###

This implementation was developed using Python and one of its libraries called networkx [^1].

## Overlaph Layout Graph Definition

>A graph is an overlap if its vertices may be put into a one-to-one correspondence with intervals on a line, such that two vertices are adjacent iff there intervals partially overlap, that is, they have non-empty intersection, but neither contains the other. [^2]

DNA sequencing devices are limited and there is not yet a device that can read all DNA at once. That's why a technique called shotgun sequencing is used. In the shotgun technique, DNA is fragmented into very small pieces. These fragments are called inserts and DNA sequencing devices read these fragments.

In the list of genomes, the genome reads are compared with each other to organize them into a single genome. During this comparison, the suffix of one genome is compared with the prefix of the other (source node's suffix and the destination node's prefix.). Every genome reads are the nodes. How many matches are provided between these nodes, they are matched by connecting with the edges that has weight according to matches. This process is repeated for all the genomes in the list, and they are all linked together in this way. As a result, directed graph is created for the first phase. 

In the Overlap Layout graph method, the hamiltonian path is used. In the Hamiltonian path method, all nodes are visited and only once necessarily. As the second phase, a gene sequence is created by circulating all the genomes/nodes, including the prefixes and suffixes once.

    TCTA**TATCTCG**
        **TATCTCG**ACTC

        TAT**CTCGACTC**
           **CTCGACTC**CTCAT

    TCTATATCTCG ---(7)---> TATCTCGACTC ---(8)---> CTCGACTCCTCAT

## Method Evaluation

There are two methods which are de bruijn graph and overlap graph to read a DNA. Overlap Graph have disadvantages compared to other graph path algorithms. It becomes more complicated with larger k-mers and also larger data sets. That means it becomes more complex with big data.

## Complexity and Speed

![Speed of the implementation as shown in the graph.](https://github.com/isilypici/BioinformaticsOverlapGraph/blob/main/speedimage.jpeg)


 
 [^1]: [Networkx](https://networkx.org/documentation/stable/index.html)
 [^2]: [Reference](https://www.graphclasses.org/classes/gc_913.html)





# Bioinformatics Overlap Layout Graph Implementation

### work in progress ###

This implementation was developed using Python and one of its libraries called [^1].

## Overlaph Layout Graph

>A graph is an overlap if its vertices may be put into a one-to-one correspondence with intervals on a line, such that two vertices are adjacent iff there intervals partially overlap, that is, they have non-empty intersection, but neither contains the other. [^2]

In a list of genomes, the genome reads are compared with each other to organize them into a single genome. During this comparison, the suffix of one genome is compared with the prefix of the other. Every genome reads are the nodes. How many matches are provided between these nodes, they are matched by connecting with the edges that has weight according to matches. This process is repeated for all the genomes in the list, and they are all linked together in this way. As a result, directed graph is created for the first phase. 

In the Overlap Layout graph method, it is necessary to visit every node on this graph. As the second phase, a gene sequence is created by circulating all the genomes/nodes, including the prefixes and suffixes once.

    TCTA**TATCTCG**
        **TATCTCG**ACTC

        TAT**CTCGACTC**
           **CTCGACTC**CTCAT

    TCTATATCTCG ---(7)---> TATCTCGACTC ---(8)---> CTCGACTCCTCAT



 
 [^1]: [Networkx](https://networkx.org/documentation/stable/index.html)
 [^2]: [Reference](https://www.graphclasses.org/classes/gc_913.html)

### TODO ###



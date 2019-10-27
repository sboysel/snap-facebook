import facebook as fb
import networkx as nx
import numpy as np

print("Loading Network (SNAP/ego-Facebook)")
fb.load_network()
print("-" * 40)
print("Complete Network")
print("Order = %d" % fb.network.order())
print("Size = %d" % fb.network.size())
print("-" * 40) 

def chain_sample(G, n, initial_node_id=None):
    
    S = nx.Graph()
    
    if initial_node_id is None:
        i = np.random.choice(list(G))
    elif isinstance(initial_node_id, int):
        i = initial_node_id
    else:
        i = list(G)[0]
        print("initial_node_id should be integer or None.  Defaulting to %d." % i)
    
    S.add_node(i)
    S.nodes[i]['features'] = G.nodes[i]['features']
    while S.order() < n:
        j = np.random.choice([nb for nb in G.neighbors(i)])
        S.add_edge(i, j)
        S.nodes[j]['features'] = G.nodes[j]['features']
        i = j
    return S


sample_sizes = [10, 100, 1000]
for n in sample_sizes:
    S = chain_sample(fb.network, n)
    print("Snowball Network (n = %d)" % n)
    print("Order = %d" % S.order())
    print("Size = %d" % S.size())
    print("-" * 40) 


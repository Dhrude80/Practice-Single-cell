import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import anndata as ad
from scipy.spatial import KDTree
rng = np.random.default_rng()

Y = np.random.randint(low=0, high=21, size=((2,100)))
adata = ad.AnnData(X=Y.T)
adata.obs["Number"] = np.random.randint(low=1, high = 30, size=100)
adata.obs["Cell_type"] = rng.choice(["T-cell","Monocyte","B-cell"], size=100)
adata.obs["XCoordinates"] = rng.uniform(0,30, size=100)
adata.obs["YCoordinates"] = rng.uniform(0,30, size=100)
mask = (adata.obs["Cell_type"] == "T-cell") 
Connections = adata[mask]
Conditions = [
    Connections.obs["Number"] <= 10,
    (Connections.obs["Number"] > 10) & (Connections.obs["Number"] < 20),
    Connections.obs["Number"] < 30
]
Colours = ["skyblue","green","yellow"]
my_colours = np.select(Conditions, Colours, default = "gray")
coords = Connections.obs[["XCoordinates","YCoordinates"]]
Coords = coords.to_numpy()
print(Coords.shape)

tissue = KDTree(Coords)
connections_in_range = tissue.query_ball_point(Coords,r=10)
adj_dict = dict(enumerate(connections_in_range))
G = nx.from_dict_of_lists(adj_dict)
G.remove_edges_from(nx.selfloop_edges(G))
nx.draw(G,pos = dict(enumerate(Coords)), node_size = 10, node_color = my_colours, edge_color = "red")
plt.show()


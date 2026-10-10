import pandas as pd
import numpy as np
import anndata as ad

# Creating some data (from internet)
metadata_dict = {
    "cell_type": ["T-cell", "B-cell", "T-cell", "Monocyte"],
    "pct_mito": [7.1, 7.4, 2.5, 4.1]
}

# represent the index or the row names
barcodes = ["Cell_A", "Cell_B", "Cell_C", "Cell_D"]

df = pd.DataFrame(metadata_dict, index=barcodes)
df.head(2)
df.info()
df.shape
df["cell_type"].value_counts()  
mask = (df["cell_type"] == "T-cell") & (df["pct_mito"] < 5)
print(df[mask])
print("-----------")
print()
X = np.array([[4,0,2,6], [0,1,0,3], [5,5,0,0]])
rows_mean = np.mean(X, axis=1)
column_sum = np.sum(X, axis=0)

adata = ad.AnnData(X=X.T)
adata.obs["cell_type"] = ["T-cell","B-cell","T-cell","Monocyte"]
adata.obs["some_numbers"] = [2,3,1,4]
mask = (adata.obs["cell_type"] == "T-cell") & (adata.obs["some_numbers"] < 3)
print(adata[mask])
X_recovered = adata.X
print()
print("original")
print(X)
print("Actual thing")
print(adata)
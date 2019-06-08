##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
Dataset['suma'] =Dataset['_c0']+Dataset['_c2']

print(Dataset)

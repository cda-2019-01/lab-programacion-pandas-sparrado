##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
Consulta = Dataset.groupby("_c1").agg({'_c2': np.max})


print(Consulta.iloc[:,0])


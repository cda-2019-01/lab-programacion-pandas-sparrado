##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
Consulta = pd.Series(Dataset.groupby("_c1").size(),name="_c0")


print(Consulta)
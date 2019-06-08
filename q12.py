##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

import pandas as pd
import numpy as np
import datetime
pd.set_option('display.notebook_repr_html', False)

Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
Dataset2 =  pd.read_csv("tbl2.tsv", sep="\t")
DataSetConbine = Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
Consulta =  pd.merge(Dataset, Dataset2, on='_c0')
Resultado = df2 = Consulta.groupby('_c5a').agg({'_c5b': np.sum})
print(Resultado.iloc[:,0])


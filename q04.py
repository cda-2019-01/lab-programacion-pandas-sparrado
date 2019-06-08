##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
Dataset =  pd.read_csv("tbl1.tsv", sep="\t")
Consulta = Dataset[["_c4"]]
ListaDeValores = Consulta._c4.unique()
ListaDeValores.sort()
ListaDeValores = [letra.upper() for letra in ListaDeValores]
print(ListaDeValores)


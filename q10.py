##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.notebook_repr_html', False)

Dataset =  pd.read_csv("tbl1.tsv", sep="\t")
Consulta = Dataset[["_c0","_c4"]]
ListaDeValores = Consulta._c0.unique()
ListaDeValores = ListaDeValores.tolist()
ListaDeValores.sort()
ListaDeResultados = []

for LetraC in ListaDeValores:
    ConsultaParaLetraActual = (Consulta[Consulta['_c0'] == LetraC])
    ConsultaSoloValoresC2 = ConsultaParaLetraActual['_c4']
    ListaDeValoresC2 = (ConsultaSoloValoresC2.tolist())
    ListaDeValoresC2.sort()
    ListaDeValoresPorString = ","
    ListaDeValoresPorString = ListaDeValoresPorString.join(ListaDeValoresC2)
    ListaDeResultados.append(ListaDeValoresPorString)
Resultado = df2 = pd.DataFrame({"_c0":ListaDeValores,"lista":ListaDeResultados})
print(Resultado)

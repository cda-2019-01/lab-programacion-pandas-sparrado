##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.notebook_repr_html', False)

Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
Consulta = Dataset[["_c1","_c2"]]
ListaDeValores = Consulta._c1.unique()
ListaDeValores = ListaDeValores.tolist()
ListaDeValores.sort()
ListaDeResultados = []

for LetraC in ListaDeValores:
    ConsultaParaLetraActual = (Consulta[Consulta['_c1'] == LetraC])
    ConsultaSoloValoresC2 = ConsultaParaLetraActual['_c2']
    ListaDeValoresC2 = (ConsultaSoloValoresC2.tolist())
    ListaDeValoresC2.sort()
    ListaDeValoresPorString = ":"
    ListaDeValoresPorString = ListaDeValoresPorString.join(map(str,ListaDeValoresC2))
    ListaDeResultados.append(ListaDeValoresPorString)
Resultado = df2 = pd.DataFrame({"_c0":ListaDeValores,"lista":ListaDeResultados})
print(Resultado)


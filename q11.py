##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.notebook_repr_html', False)

Dataset =  pd.read_csv("tbl2.tsv", sep="\t")
Consulta = Dataset
ListaDeValores = Consulta._c0.unique()
ListaDeValores = ListaDeValores.tolist()
ListaDeValores.sort()
ListaDeResultados = []

for LetraC in ListaDeValores:
    ConsultaParaLetraActual = (Consulta[Consulta['_c0'] == LetraC])
    ConsultaSoloValoresC2 = ConsultaParaLetraActual[['_c5a','_c5b']]
    ListaDeValoresC5=[]
    for index, row in ConsultaSoloValoresC2.iterrows():
        PegadoValoresDeCelda = row["_c5a"]+":"+str(row["_c5b"])
        ListaDeValoresC5.append(PegadoValoresDeCelda)
    ListaDeValoresC5.sort()
    ListaDeValoresPorString = ","
    ListaDeValoresPorString = ListaDeValoresPorString.join(ListaDeValoresC5)
    ListaDeResultados.append(ListaDeValoresPorString)
Resultado = df2 = pd.DataFrame({"_c0":ListaDeValores,"lista":ListaDeResultados})
print(Resultado)

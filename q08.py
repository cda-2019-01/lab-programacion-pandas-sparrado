##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.notebook_repr_html', False)
Dataset =  pd.read_csv("tbl0.tsv", sep="\t")
DataAno = (Dataset[["_c3"]])
DataAno = DataAno.iloc[:,0]
DataSerie = pd.Series(DataAno).tolist()
DataSerie = [ano[:4] for ano in DataSerie]
Dataset["ano"] = DataSerie
print(Dataset)

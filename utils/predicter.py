import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
import numpy as np

#dada una muestra devuelve un array [p0,p1] donde p0 es la probabilidad
#de la clase 0 (sano) y p1 la probabilidad de la clase 1 (enfermo)
def predict(sample=[]):
    #leer los datos del archivo .csv
    #data = pd.read_csv(os.getcwd()[:-5] + "/data/heart.csv")
    data = pd.read_csv(os.getcwd() + "/data/heart.csv")
    
    #renombrar para mejor entendimiento
    data.rename(columns={'age':'edad', 
                         'sex':'sexo', 
                         'cp':'tipo de dolor pectoral',
                         'trestbps':'tension en reposo', 
                         'chol': 'colesterol',
                         'fbs':'glucemia en ayunas', 
                         'restecg':'electrocardiograma',
                         'thalach':'ppm maximas',
                         'exang':'angina inducida',
                         'oldpeak':'depresion ST',
                         'slope':'pendiente',
                         'ca':'nº vasos mayores',
                         'thal': 'thal'
                         },                    
                inplace=True)
    
    #separar la última columna
    X = data.drop(['target'], axis=1)
    y = data.loc[:, 'target']
    
    #entrenar modelo con los parámetros óptimos con todos los datos
    clf = LogisticRegression(
        penalty= 'l2',solver='liblinear', C=0.6158, random_state=0).fit(X, y)
    
    #devolver probabilidades de cada clase
    return clf.predict_proba(sample)

'''
sample = np.array([40,1,1,1,1,1,1,1,1,1,1,1,1])
print(predict(sample.reshape(1,-1)))
'''


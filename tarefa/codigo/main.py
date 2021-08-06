import pickle
from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age: float, Lifeboat: int, Pclass: int):
    with open(f'{os.path.dirname(__file__)}/model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
        ## Cria o dataframe para enviar para o modelo (ordena os parametros alfabeticamente)
        df = pd.DataFrame([[Age, Lifeboat, Pclass, Sex]], columns =['Age', 'Lifeboat', 'Pclass', 'Sex'])
        ## Realiza a predição (TODO: tratar exceções)
        y = titanic.predict(df)
        survived = bool(y[0])
        response = {
            "survived": survived,
            "status": 200,	
            "message": "Sobreviveu!" if survived else "Não sobreviveu!",	
        }
        return response

@app.get('/model')
def get():
    return {'hello':'test'}

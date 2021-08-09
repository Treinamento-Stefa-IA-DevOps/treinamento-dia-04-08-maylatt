import pickle
from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age: float, Lifeboat: int, Pclass: int):
    # Validação dos atributos, retorna Bad Request caso algum atributo seja inválido
    if (Sex not in [0, 1]) :
        raise HTTPException(status_code=400, detail="Sexo invalido!")
    if (Age < 0) :
        raise HTTPException(status_code=400, detail="Idade invalida!")
    if (Pclass not in [1, 2, 3]) :
        raise HTTPException(status_code=400, detail="Classe invalida!")

    try:
        ## Abre o arquivo que contém o modelo usa caminho completo para evitar erro de referência 
        with open(f'{os.path.dirname(__file__)}/model/Titanic.pkl', 'rb') as fid: 
            ## Carrega o modelo
            titanic = pickle.load(fid)
            ## Cria o dataframe para enviar para o modelo (ordena os parametros alfabeticamente)
            df = pd.DataFrame([[Age, Lifeboat, Pclass, Sex]], columns =['Age', 'Lifeboat', 'Pclass', 'Sex'])
            ## Realiza a predição
            y = titanic.predict(df)
            survived = bool(y[0])
            response = {
                "survived": survived,
                "status": 200,	
                "message": "Sobreviveu!" if survived else "Não sobreviveu!",	
            }
            return response
    except EnvironmentError: 
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno. Tente novamente!")


@app.get('/model')
def get():
    return {'hello':'test'}

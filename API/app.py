from flask import Flask, jsonify, request
import joblib
import warnings

import pickle
from tensorflow.keras.models import load_model

import pandas as pd

warnings.filterwarnings("ignore")

with open(r"/home/vinicius/Documentos/Repositorios/Machine-Learning-Braco-Robotico/API/scaler.pkl", "rb") as arquivo:
    # Carregar o objeto pickle do arquivo
    scaler = pickle.load(arquivo)

modelo = load_model("/home/vinicius/Documentos/Repositorios/Machine-Learning-Braco-Robotico/API/modelo.h5")

colunas_entrada = ['Amplitude_degrau', 'RiseTime', 'SettlingTime', 'Overshoot']
colunas_saida = ['Kp', 'Ti', 'Td', 'b', 'c', 'Tf']

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Recebe os dados no formato JSON
        dados_entrada = request.get_json()

        # Converte o dict em um array numpy
        entrada = pd.DataFrame(dados_entrada, index=[0])

        # Realiza a escala dos dados de entrada
        entrada_scaled = scaler.transform(entrada)

        # Faz a previsão usando o modelo
        saida_scaled = modelo.predict(entrada_scaled)

        resultado = dict(zip(colunas_saida, saida_scaled.flatten().tolist()))

        # Arredondar cada valor para 4 casas decimais
        resultado_arredondado = {coluna: round(valor, 4) for coluna, valor in resultado.items()}    

        return jsonify(resultado_arredondado) , 200

    except Exception as e:
        return jsonify({'erro': str(e)}) , 500

if __name__ == '__main__':
    app.run(debug=True)

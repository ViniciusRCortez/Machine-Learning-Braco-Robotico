import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd

with open("/home/vinicius/Documentos/Repositorios/Machine-Learning-Braco-Robotico/API/modelo.pkl", "rb") as arquivo:
  modelo=pickle.load(arquivo)


# Suponha que você tem uma nova linha de entrada não normalizada que deseja prever
new_input = pd.DataFrame({
    'Amplitude_degrau': [200],
    'RiseTime': [2],
    'SettlingTime': [5],
    'Overshoot': [15]
})

# Pré-processamento da linha de entrada (aplique a mesma normalização)
new_input_normalized = scaler.transform(new_input)  # Use o mesmo scaler que foi usado para normalizar os dados de treinamento

# Faça a previsão
predicted_output = modelo.predict(new_input_normalized)  # Realiza a previsão com a RNA treinada

# Crie um DataFrame com rótulos de coluna
predicted_df = pd.DataFrame(predicted_output, columns=colunas_saida)  # "colunas_saida" é uma lista de nomes de colunas de saída

# Exiba o DataFrame com os valores previstos
print("Valores Preditos:")
print(predicted_df)
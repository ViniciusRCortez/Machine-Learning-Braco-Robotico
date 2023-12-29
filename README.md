# Machine Learning para Controle de Braço Robótico

Este repositório contém o código-fonte e os modelos desenvolvidos como parte de um projeto de conclusão de curso que envolve a aplicação de Machine Learning para estimar os parâmetros de um controlador PID-2DOF. Esse controlador é utilizado para o controle de um dos motores do braço robótico presente no GPAR da UFC (Campus do Pici).

## Descrição do Projeto

O projeto visa aprimorar o controle de um braço robótico por meio da implementação de técnicas de Machine Learning. O modelo de rede neural utilizado foi treinado para estimar os parâmetros do controlador PID-2DOF com base em dados de entrada, como amplitude de degrau, tempo de subida (RiseTime), tempo de acomodação (SettlingTime) e overshoot.

## Estrutura do Repositório

- `TCC.pdf`: Projeto de conclusão de curso que gerou o modelo proposto.
- `modelo.pkl`: Modelo de Machine Learning treinado (pickle).
- `modelo.h5`: Modelo da rede neural (Keras HDF5).
- `scaler.pkl`: Objeto de escalonamento utilizado para normalizar os dados.
- `API/`: Diretório contendo o código-fonte da API desenvolvida.
  - `app.py`: Arquivo principal da API.
  - `requirements.txt`: Lista de dependências do projeto.

## API para Previsão de Parâmetros PID

A API desenvolvida permite realizar previsões dos parâmetros do controlador PID-2DOF com base em dados de entrada fornecidos via solicitações POST. A seguir, estão alguns endpoints principais:

### `/api/hello` (Método GET)

Retorna uma mensagem de saudação "Hello, world!".

### `/api/predict` (Método POST)

Retorna um json com a predição dos dados enviados.

Exemplo de uso:
```bash
curl http://localhost:5000/api/predict
request.body = 
{
  "Amplitude_degrau": 200,
  "RiseTime": 2,
  "SettlingTime": 5,
  "Overshoot": 15
}

response.body = 
{
    "Kp": 0.0838,
    "Td": 0.3513,
    "Tf": 0.6285,
    "Ti": 0.7741,
    "b": 0.24,
    "c": 0.2896
}


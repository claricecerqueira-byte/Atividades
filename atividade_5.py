#RESPOSTAS DA ATIVIDADE 5:

#PERGUNTA 1:
import requests

def obter_cotacao_dolar():
    # define a URL que será consultada
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"

    try:
        # Faz a requisição à API
        resposta = requests.get(url)
        resposta.raise_for_status() #ver se teve alguma erro, verifica o código da requisição

        # Converte a resposta para JSON
        dados = resposta.json()
 # Extrai apenas o valor atual (bid/compra) da moeda
        valor_dolar = dados["USDBRL"]["bid"]

        # Exibe apenas o valor
        print(valor_dolar)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")

if __name__ == "__main__":
    obter_cotacao_dolar()

#PERGUNTA 2:
import requests
import json


def consultar_api_github():
    # define qaul URL será consultada
    url = "https://api.github.com"

    try:
        # Faz a requisição GET à API
        resposta = requests.get(url)
        resposta.raise_for_status() # Verifica se o código da requisição foi bem-sucedida (código 200)

        # Converte a resposta para um JSON
        dados = resposta.json()
 # Exibe os dados retornados de forma formatada e indentada para facilitar a leitura
        print("Dados retornados pela API do GitHub:")
        print(json.dumps(dados, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")


if __name__ == "__main__":
    consultar_api_github()

#PERGUNTA 3:
import json

# Pergunta e resposta
dados = {
    "pergunta": "O que é IA?",
    "resposta": "É Inteligência Artificial.Ela é criada para automatizar processos."
}

# Coloca os dados no formato JSON
resultado_json = json.dumps(dados, ensure_ascii=False)
# Exibe o resultado na tela
print(resultado_json)

#PERGUNTA 4:
url = "https://restcountries.com/v3.1/name/brazil"
resposta = requests.get(url)

dados = resposta.json()[0]
print("Nome:", dados["name"]["common"])
print("Capital:", dados["capital"][0])
print("População:", dados["population"])

#PERGUNTA 5
pessoa = {
    "nome": "Marcela Luiz",
    "idade": 21
}

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])

#PERGUNTA 6:
import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=-10.91&longitude=-37.07&current_weather=true"

resposta = requests.get(url)
dados = resposta.json() #transforma em JSON

temperatura = dados["current_weather"]["temperature"]
vento = dados["current_weather"]["windspeed"]

print(f"Temperatura: {temperatura}°C")
print(f"Velocidade do Vento: {vento} km/h")

temperatura_vento = {
    "temperatura": temperatura,
    "vento": vento
}

with open("dados_api.json", "w") as arquivo:
    json.dump(temperatura_vento, arquivo, indent=4)

print("\nArquivo 'dados_api.json' salvo com sucesso!")

#PERGUNTA 7:
import json
pergunta = input("Digite sua pergunta: ")

dados = {
    "pergunta": pergunta,
    "resposta": "Esta é uma resposta automática."
}

print(json.dumps(dados, indent=4, ensure_ascii=False))
with open("pergunta_resposta.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)
arquivo.close()

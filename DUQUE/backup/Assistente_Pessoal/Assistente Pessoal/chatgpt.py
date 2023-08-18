import requests
import json

API_KEY_CHATGPT = "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"

headers = {"Authorization": f"Bearer {API_KEY_CHATGPT}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"


pedra = 1

while pedra == 1:

    pergunta = input('Pergunte: ')

    if pergunta >= '':

        body_mensagem = {
            "model": id_modelo,
            "messages": [{"role": "user", "content": f"{pergunta}"}]
        }

        body_mensagem = json.dumps(body_mensagem)

        requisicao = requests.post(link, headers=headers, data=body_mensagem)
        #print(requisicao)
        resposta = requisicao.json()
        mensagem = resposta["choices"][0]["message"]["content"]
        print(mensagem)


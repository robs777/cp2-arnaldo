from flask import Flask, render_template, request,url_for
import requests


app = Flask(__name__)

@app.route('/receitas')
def receitas():
    response = requests.get('https://gold-anemone-wig.cyclic.app/receitas/todas')
    data = response.json()
    return render_template('receitas.html', receitas=data)

import requests

@app.route('/pesquisa')
def buscar_receitas_por_ingrediente(ingrediente):
  # Faz a requisição à API
  url = "https://gold-anemone-wig.cyclic.app/receitas/todas"
  resposta = requests.get(url)

  # Verifica se a requisição foi bem sucedida
  if resposta.status_code == 200:
    # Converte o JSON da resposta em um dicionário
    dados = resposta.json()
    # Filtra as receitas que contêm o ingrediente
    receitas_com_ingrediente = []
    for receita in dados:
      if ingrediente.lower() in receita["ingredientes"].lower():
        receitas_com_ingrediente.append(receita)

    return receitas_com_ingrediente
  else:
    # Erro na requisição à API
    print(f"Erro na requisição à API: {resposta.status_code}")
    return []

# Exemplo de uso
ingrediente_pesquisado = input("Digite o ingrediente que você procura: ")
receitas_encontradas = buscar_receitas_por_ingrediente(ingrediente_pesquisado)

if receitas_encontradas:
  print(f"Receitas encontradas com o ingrediente {ingrediente_pesquisado}:")
  for receita in receitas_encontradas:
    print(f"- {receita['receita']}")
else:
  print(f"Não foram encontradas receitas com o ingrediente {ingrediente_pesquisado}.")


if __name__ == '__main__':
    app.run(debug=True)

from dataclasses import dataclass
import requests

@dataclass
class Receita:
    ingrediente: str

    def exibir(self):
        print(f"Ingrediente: {self.ingrediente}")

def buscar_receita(ingrediente):
    # Assuming the API endpoint supports querying by ingredient
    url = f"https://gold-anemone-wig.cyclic.app/receitas/todas{ingrediente}"
    response = requests.get(url)
   

ingrediente = input("Digite o ingrediente: ")

receita = buscar_receita(ingrediente)

if receita:
    receita.exibir()
else:
    print("Receita não encontrada.")




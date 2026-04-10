import pandas as pd
from faker import Faker
import random
import os

fake = Faker('pt_BR') # Gera dados em portugues
os.makedirs("Projeto", exist_ok=True) # Cria a pasta se ela ainda não existir

def salvar_tabela(df, nome_arquivo):
    caminho = f"Projeto/{nome_arquivo}.csv" # Salva a planilha como CSV
    versao = 1
    novo_caminho = caminho
    while os.path.exists(novo_caminho):
        versao += 1 
        novo_caminho = f"Projeto/{nome_arquivo}_V{versao}.csv"# Se o arquivo já existir ele incrementa junto a variavel versão
    
    df.to_csv(novo_caminho, index=False, sep=';', encoding='utf-8-sig')
    print(f"Arquivo salvo: {novo_caminho}")

lojas = []

for i in range(1,36):
    lojas.append({
        "id_loja": 100 + i,
        "nome_loja": f"Luminix {fake.city()}",
        "cidade": fake.city(),
        "estado": fake.state_abbr(),
        "gerente": fake.name()
    })

df_lojas = pd.DataFrame(lojas)  #Converte a lista em planilha
salvar_tabela(df_lojas, "lojas")

vendedores = []

for i in range (1,51):
    vendedores.append({
        "id_vendedor": 1000 + i,
        "nome": fake.name(),
        "id_loja": random.choice(df_lojas["id_loja"]),
        "data_admissao": fake.date_between(start_date='-5y', end_date='today'),
        "meta_mensal": round(random.uniform(3000, 15000))
    })

df_vendedores = pd.DataFrame(vendedores)
salvar_tabela(df_vendedores, "vendedores")

vendas = []

for i in range (1,451):
    vendedor_escolhido = random.choice(df_vendedores["id_vendedor"].tolist()) # Converte a coluna em lista
    loja_vendedor = df_vendedores.loc[df_vendedores["id_vendedor"] == vendedor_escolhido, "id_loja"].values[0] # Identificar e retorna o vendedor escolhido
    vendas.append({
        "id_venda": 10000 + i,
        "id_vendedor": vendedor_escolhido,
        "id_loja": loja_vendedor,
        "data_venda":fake.date_between(start_date='-1y', end_date='today'),
        "valor": round(random.uniform(50, 5000), 2),
        "forma_pagamento": random.choices(["Pix", "Crédito", "Débito"], weights=[0.6, 0.3, 0.1], k=1)[0] # Probabilidades definidas
    })

df_vendas = pd.DataFrame(vendas)
salvar_tabela(df_vendas, "vendas")

import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# 1. Gerar dados fictícios simulando a imagem
print("Gerando dados...")
datas = pd.date_range(start='2017-01-01', end='2019-12-31', freq='D')
marcas = ['Adventure Works', 'Proseware', 'Contoso', 'Fabrikam', 'Litware']
continentes = ['North America', 'Europe', 'Asia']

data_list = []
for data in datas:
    # Criamos 3 a 5 vendas por dia
    for _ in range(np.random.randint(3, 6)):
        venda = np.random.uniform(1000, 5000)
        lucro_percent = np.random.uniform(0.4, 0.6) # Margem perto de 50% como na foto
        data_list.append({
            'data_venda': data,
            'marca': np.random.choice(marcas),
            'continente': np.random.choice(continentes),
            'valor_venda': round(venda, 2),
            'custo': round(venda * (1 - lucro_percent), 2)
        })

df = pd.DataFrame(data_list)

# 2. Conectar ao PostgreSQL
# Formato: postgresql://usuario:senha@localhost:porta/nome_do_banco
engine = create_engine('postgresql://postgres:sua_senha@localhost:5432/sales_db')

# 3. Enviar para o Banco de Dados
print("Enviando para o SQL...")
df.to_sql('vendas', engine, if_exists='replace', index=False)
print("Sucesso!")
# 📊 Sales Analytics Dashboard - Full Stack Data Project

Este projeto consiste em um ciclo completo de análise de dados, desde a geração de dados e armazenamento em banco de dados relacional até a visualização executiva em um Dashboard de alto nível.

## 🚀 Tecnologias Utilizadas

* **Python:** Geração de dados sintéticos e lógica de ETL.
* **Pandas & SQLAlchemy:** Manipulação de dados e integração com banco de dados.
* **PostgreSQL:** Armazenamento robusto dos dados de vendas.
* **Power BI:** Criação de dashboard interativo com design Dark Mode.
* **SQL:** Estruturação de tabelas e consultas.

## 🛠️ Estrutura do Projeto

1.  **/data**: Pasta contendo (opcionalmente) os arquivos CSV gerados.
2.  **/scripts**: Script Python `etl_process.py` que gera os dados e os envia para o Postgres.
3.  **Dashboard.pbix**: Arquivo do Power BI com o design final.

## 📉 Visualizações Chave
O dashboard foca em 3 pilares principais:
* **Financeiro:** Total Vendido, Lucro Total e Margem de Lucro (%).
* **Temporal:** Evolução de vendas entre 2017 e 2019.
* **Competitivo:** Ranking de performance por Marca e Continente.

## 🔧 Como Executar

1. **Configurar o Banco de Dados:**
   No PostgreSQL, crie um banco chamado `sales_db`:
   ```sql
   CREATE DATABASE sales_db;
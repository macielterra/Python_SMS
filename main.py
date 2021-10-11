# instalar o Pandas / Openpyxl / Twilio
# Passos para Solução
# Abrir os 6 arquivos em Excel
# Para cada arquivo:
 # Verificar se algum valor na coluna Vendas for maior que R$ 55.000
 # Se for maior de R$ 55.000 -> Enviar um SMS para meu dispositivo mobile, 
 # Informando o Nome, o mês e as vendas do Vendedor
import pandas as pd
from twilio.rest import Client
# Código do TWilio para enviar SMS
account_sid = 'ACa0a585b9ecc3faa77c90c5b02338a69f'
auth_token = 'bc9452ac7e3ed8e888161d3f058f8caf'
client = Client(account_sid, auth_token) 
lista_meses = ['janeiro','fevereiro','marco','abril','maio','junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xls')
    if (tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} o funcionario {Vendedor} bateu a meta em R${Vendas}')
        message = client.messages.create(
            to='+5551998481992',
            from_='+13157582690',
            body= f'No mês {mes} o funcionario {Vendedor} bateu a meta em R$ {Vendas}')      
        print(message.sid)


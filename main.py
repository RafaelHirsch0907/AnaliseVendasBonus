import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC841a174bb9bc540a65ed8b7b5f5e4cf3"
# Your Auth Token from twilio.com/console
auth_token  = "48d8c315d99db2a4ac5f1113d298f318"
client = Client(account_sid, auth_token)


listaMeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in listaMeses:      # for variavel in lista     identação é importante no Python
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')         # f '{}'  formatar algo que será dinâmico dentro do código
    if (tabelaVendas['Vendas'] > 55000).any():
        vendedor = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendedor'].values[0]     # .loc  localizar algo passando as colunas nos [] OBS: ele te responde em formato e tabela. Para contornar isso utilizar.values[0]
        vendas = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendas'].values[0]
        print()
        message = client.messages.create(
            to="+5571992650907",
            from_="+18023922483",
            body=f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)





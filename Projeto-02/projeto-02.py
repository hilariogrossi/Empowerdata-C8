import yfinance
import matplotlib
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input('Digite o código da ação desejada: ')
data_inicio = input('Digite a data inicial da ser buscada [0000-00-00 (ano, mês, dia)]: ')
data_final = input('Digite a data final da ser buscada [0000-00-00 (ano, mês, dia)]: ')

dados = yfinance.Ticker(ticker).history(start='2024-01-01', end='2024-08-07')

fechamento = dados.Close # Valor de fechamento de mercado
fechamento.plot() # Produz o gráfico

valor_maximo = round(fechamento.max(), 2)
valor_minimo = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

'''print('-' * 70)
print(f'O valor mínimo da ação {ticker} no período solicitado é R$ {valor_minimo}.')
print('-' * 70)
print(f'O valor máximo da ação {ticker} no período solicitado é R$ {valor_maximo}')
print('-' * 70)
print(f'O valor médio da ação {ticker} no período solicitado é R$ {valor_medio}')
print('-' * 70)'''

# time.sleep(5)
# pyautogui.position()

destinatario = 'hilariogrossi@yahoo.com.br'
descricao_email = 'Seguem análises solicitadas'
mensagem_email = f'''
Prezado Gestor,

Seguem as análises solicitadas da ação {ticker}.

Data de início: {data_inicio}
Data final: {data_final}

Cotação máxima...: R$ {valor_maximo}
Cotação mínima...: R$ {valor_minimo}
Cotação médio......: R$ {valor_medio}


Qualquer dúvida estarei à disposição.

Atenciosamente,

Hilário Grossi de Oliveira.'''

webbrowser.open('www.gmail.com')
time.sleep(5)
pyautogui.click(x=96, y=211)

pyautogui.PAUSE = 3

pyautogui.click(x=1207, y=414)
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyperclip.copy(descricao_email)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyperclip.copy(mensagem_email)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(x=1126, y=973)

pyautogui.click(x=1892, y=26)

print('Email enviado com sucesso!')

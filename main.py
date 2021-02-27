import requests
token = '1542527465:AAGXxvrAMBQEmLNgsoSPHusID37ERH7Esoc'
url = f'https://api.telegram.org/bot{token}/sendMessage'
chatId = '856324152'

r = requests.get('https://apiprevmet3.inmet.gov.br/previsao/4105805')
result = r.json()

dt = result['4105805']

keys = [] 
for key in dt.keys():
    keys.append(key)

message = ""
count = 0
for indice in keys:
    if count < 2:
        message += f'*{indice}*\n'
        message += f'*Manhã*\n'
        message += f'{dt[indice]["manha"]["resumo"]} {dt[indice]["manha"]["temp_min"]}Cº - {dt[indice]["manha"]["temp_max"]}Cº\n'
        message += f'*Tarde*\n'
        message += f'{dt[indice]["tarde"]["resumo"]} {dt[indice]["tarde"]["temp_min"]}Cº - {dt[indice]["tarde"]["temp_max"]}Cº\n'
        message += f'*Noite*\n'
        message += f'{dt[indice]["noite"]["resumo"]} {dt[indice]["noite"]["temp_min"]}Cº - {dt[indice]["noite"]["temp_max"]}Cº\n\n'
    else:
        message += f'*{indice}*\n'
        message += f'{dt[indice]["resumo"]} {dt[indice]["temp_min"]}Cº - {dt[indice]["temp_max"]}Cº\n\n'

    count += 1

data = {'chat_id': chatId, 'text': message, 'parse_mode': 'Markdown'}
requests.post(url, data).json()
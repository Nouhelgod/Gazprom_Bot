import json
from responseParser import Response

with open('settings.json', encoding='utf-8') as file:
    settings = json.load(file)
    

def getReply(reply: str, code: str = '') -> str:
    if reply == 'welcome':
        message = \
        'Этот бот поможет Вам проверить любую компанию на наличие в черных' +\
        'списках налоговой и ЦБ и предоставить отчет о компании' + '\n' +\
        'Для старта проверки, отправьте ИИН или ОГРН интересующей компании в чат.'
        
    if reply == 'wrong':
        message = 'Введите корректный номер ИНН или ОГРН.'
        
    if reply == 'makeRequest':
        response = Response(code)
        message = str(response)
        
    return message
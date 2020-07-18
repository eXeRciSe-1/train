from bottle import route, request, run
from num2words import num2words


@route ('/num2text/', method = 'POST' )

def num_text():
    #Запрос
    json_data =  request.json
    # Проверяем наличие необходимого ключа в запросе
    if 'number' not in json_data:
        return ('The key number doesn`t exist')
    number = json_data ['number']
    #Переводим числовые данные в текст
    text = num2words(number, lang='ru')


    return text


run(debug=True)
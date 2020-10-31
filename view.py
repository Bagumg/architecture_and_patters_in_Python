from core.render import render


def index_view(request):
    print('Это request из view ', request)
    secret = request.get('secret_key', None)
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('about.html', secret=secret)


def contact_view(request):
    # print(request)
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']

        with open('data_log.txt', 'w', encoding='utf-8') as log_file:
            log_file.write(f'Получено сообщение от {email}, тема сообщения {title} текст сообщения {text}')

        print(f'Получено сообщение от {email}, тема сообщения {title} текст сообщения {text}')
        return '200 OK', render('success.html')
    else:
        return '200 OK', render('contact.html')

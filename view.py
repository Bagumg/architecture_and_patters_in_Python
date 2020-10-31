from core.render import render


def index_view(request):
    secret = request.get('secret_key', None)
    ip = request.get('ip', None)
    env = request.get('env', None)
    return '200 OK', render(
        'index.html',
        env=env,
        request=request,
        secret=secret,
        ip=ip
    )


def about_view(request):
    secret = request.get('secret_key', None)
    ip = request.get('ip', None)
    return '200 OK', render(
        'about.html',
        request=[request['secret_key'], request['ip']],
        secret=secret,
        ip=ip)


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

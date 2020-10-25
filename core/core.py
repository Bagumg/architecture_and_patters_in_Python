class MainApp:

    def __init__(self, urlpatterns, front_controllers):
        """
        :param urlpatterns: принимает словарь связок url:view
        :param front_controllers: список контроллеров
        """
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        """
        Объектом для запуска wsgi может быть любой callable объект,
        т.е. либо функция, либо метода __call__ класса.
        :param environ: словарь с данными запроса от пользователя
        :param start_response: функция для отправки кода ответа и заголовков, нужна для передачи заголовков ответа
        :return: код ответа и заголовки(start_response), тело ответа return в виде списка из набора байт
        """
        print(environ['HTTP_X_REAL_IP'])
        path = environ['PATH_INFO']
        if path in self.urlpatterns:
            view = self.urlpatterns[path]
            request = {}
            for controller in self.front_controllers:
                controller(request, environ)
            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'Page Not Found']

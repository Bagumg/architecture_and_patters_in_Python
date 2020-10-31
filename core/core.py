class MainApp:

    def parse_get_data(self, data):
        # print(data)
        result = dict()
        if data:
            params = data.split('&')
            # print(params)
            for item in params:
                k, v = item.split('=')
                # print(k)
                # print(v)
                result[k] = v
        return result

    def parse_wsgi_input_data(self, data):
        result = dict()
        if data:
            data_str = data.decode('utf-8')
            result = self.parse_get_data(data_str)
        return result

    def get_wsgi_input_data(self, environ):
        data_content_length = environ.get('CONTENT_LENGTH')
        content_length = int(data_content_length) if data_content_length else 0
        data = environ['wsgi.input'].read(content_length) if content_length else b''
        return data

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
        # print(environ['HTTP_X_REAL_IP'])
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'

        method = environ['REQUEST_METHOD']
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        query_string = environ['QUERY_STRING']
        request_params = self.parse_get_data(query_string)

        if path in self.urlpatterns:
            view = self.urlpatterns[path]
            request = dict()
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params
            for controller in self.front_controllers:
                controller(request)
            print(request)
            code, text = view(request)
            print(text)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'Page Not Found']

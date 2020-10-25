from core.core import MainApp
import view

urlpatterns = {
    '/': view.index_view,
    '/about': view.about_view,
}


def secret_controller(request, environ):
    request['secret_key'] = 'My_secret_key'
    environ['HTTP_X_REAL_IP']
    # request['ip'] = environ['HTTP_X_REAL_IP']


front_controllers = [
    secret_controller,
]

app = MainApp(urlpatterns, front_controllers)

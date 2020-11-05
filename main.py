from core.core import MainApp
import view

urlpatterns = {
    '/': view.index_view,
    '/about/': view.about_view,
    '/contact/': view.contact_view,
}


def secret_controller(request):
    request['secret_key'] = 'My_secret_key'


def ip_controller(request, environ):
    request['ip'] = environ['HTTP_X_REAL_IP']


def environ_controller(request, environ):
    request['env'] = environ


front_controllers = [
    secret_controller,
    # ip_controller,
    # environ_controller,
]

app = MainApp(urlpatterns, front_controllers)

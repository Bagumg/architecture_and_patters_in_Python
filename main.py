from core.core import MainApp
from core.logs.logging import Logger
from models import TeachingSite
import view


urlpatterns = {
    '/': view.main_view,
    '/create-course/': view.create_course,
    '/create-category/': view.create_category,
    '/copy-course/': view.copy_course,
    '/category-list/': view.category_list
}


def secret_controller(request):
    request['secret'] = 'my_secret_key'


front_controllers = [
    secret_controller
]

app = MainApp(urlpatterns, front_controllers)

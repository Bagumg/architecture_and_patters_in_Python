from core.core import MockApplication, MainApp
from core.logs.logging import Logger, debug
from core.render import render
from models import TeachingSite
import view

site = TeachingSite()
logger = Logger('main')

urlpatterns = {
    '/': view.main_view,
    '/create-course/': view.create_course,
    '/create-category/': view.create_category,
    '/copy-course/': view.copy_course,
    '/category-list/': view.category_list
}


def secret_controller(request):
    request['secret'] = 'secret'


front_controllers = [
    secret_controller
]

app = MainApp(urlpatterns, front_controllers)

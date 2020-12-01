from core.core import MainApp
from core.logs.logging import Logger
from models import TeachingSite
import view


urlpatterns = {
    '/': view.main_view,
    '/create-course/': view.create_course,
    '/create-category/': view.CategoryCreateView(),
    '/copy-course/': view.copy_course,
    '/category-list/': view.CategoryListView(),
    '/student-list/': view.StudentListView(),
    '/create-student/': view.StudentCreateView(),
    '/add-student/': view.AddStudentByCourseCreateView(),
    '/api/': view.api_courses,
}


def secret_controller(request):
    request['secret'] = 'my_secret_key'


front_controllers = [
    secret_controller
]

app = MainApp(urlpatterns, front_controllers)

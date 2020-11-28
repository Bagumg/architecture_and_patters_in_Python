from core.utils.prototypes import PrototypeMixin


class User:
    pass


class Teacher(User):
    pass


class Student(User):
    pass


class FactoryMethod:

    def __init__(self, types=None):
        self.types = types or {}


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class CourseCategory:
    auto_id = 0

    def __init__(self, name, category):
        self.id = CourseCategory.auto_id
        CourseCategory.auto_id += 1
        self.name = name
        self.category = category
        self.courses_list = []

    def courses_count(self):
        result = len(self.courses_list)
        if self.category:
            result += self.category.courses_count()
        return result


class Course(PrototypeMixin):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)


class WebinarCourse(Course):
    pass


class VideoCourse(Course):
    pass


class CourseFactory:
    types = {
        'webinar': WebinarCourse,
        'video': VideoCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class TeachingSite:

    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    def create_user(self, type_):
        return UserFactory.create(type_)

    def create_category(self, name, category=None):
        return CourseCategory(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с таким id. {id}')

    def create_course(self, type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name) -> Course:
        for item in self.courses:
            if item.name == name:
                return item
        return None

from core.utils.observer import Subject, Observer
from core.utils.prototypes import PrototypeMixin


class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    pass


class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []


class FactoryMethod:

    def __init__(self, types=None):
        self.types = types or {}


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class CourseCategory:
    auto_id = 0

    def __init__(self, name, category):
        self.id = CourseCategory.auto_id
        CourseCategory.auto_id += 1
        self.name = name
        self.category = category
        self.courses_list = []

    def __getitem__(self, item):
        return self.courses_list[item]

    def courses_count(self):
        result = len(self.courses_list)
        if self.category:
            result += self.category.courses_count()
        return result


class Course(PrototypeMixin, Subject):

    def __init__(self, name, category):
        super().__init__()
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []

    def __getitem__(self, item):
        return self.students[item]

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)
        self.notify()


class SmsNotifier(Observer):

    def update(self, subject: Course):
        print('SMS: ', f'Студент {subject.students[-1].name} добавлен на курс')


class EmailNotifier(Observer):

    def update(self, subject: Course):
        print(('EMAIL: ', f'Студент {subject.students[-1].name} добавлен на курс'))


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

    def create_user(self, type_, name):
        return UserFactory.create(type_, name)

    def create_category(self, name, category=None):
        return CourseCategory(name, category)

    def create_course(self, type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_student(self, name) -> Student:
        for item in self.students:
            if item.name == name:
                return item

    def get_course(self, name) -> Course:
        for item in self.courses:
            if item.name == name:
                return item

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с таким id. {id}')

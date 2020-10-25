from jinja2 import Template
import os


def render(template_name, folder='templates', **kwargs):
    """
    Шаблонизатор. Осуществляет рендеринг страниц с помощью библиотеки jinja2
    :param template_name: имя шаблона
    :param folder: папка с шаблонами
    :param kwargs: параметры для передачи в шаблон
    :return: отрендериный шаблон
    """
    file_path = os.path.join(folder, template_name)
    with open(file_path, encoding='utf-8') as file:
        template = Template(file.read())
    return template.render(**kwargs)

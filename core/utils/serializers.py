import jsonpickle as jsonpickle


class BaseSerializer:

    def __init__(self, obj):
        self.obj = obj

    def save(self):
        return jsonpickle.dumps(self.obj)

    def load(self, data):
        return jsonpickle.loads(data)

    def answer(self):
        return f'This is API test string. If you see it, api works fine!'

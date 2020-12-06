class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'DataBase commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'DataBase update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'DataBase delete error: {message}')

class BusinessException(Exception):
    def __init__(self, error_code, message=None):
        if message:
            super().__init__(message)
            self.message = message
        else:
            super().__init__(error_code.message)
            self.message = error_code.message
        self.code = error_code.code
class ValidationError(Exception):
    """Базовый класс для всех ошибок валидации"""
    pass

class EmptyUsernameError(ValidationError):
    """Ошибка: пустое имя пользователя"""
    def __init__(self):
        self.message = "Имя пользователя не может быть пустым"
        super().__init__(self.message)

class PasswordTooShortError(ValidationError):
    """Ошибка: слишком короткий пароль"""
    def __init__(self):
        self.message = "Пароль должен содержать минимум 8 символов"
        super().__init__(self.message)

class PasswordNoUppercaseError(ValidationError):
    """Ошибка: в пароле нет заглавных букв"""
    def __init__(self):
        self.message = "Пароль должен содержать хотя бы одну заглавную букву"
        super().__init__(self.message)

class PasswordNoLowercaseError(ValidationError):
    """Ошибка: в пароле нет строчных букв"""
    def __init__(self):
        self.message = "Пароль должен содержать хотя бы одну строчную букву"
        super().__init__(self.message)

class PasswordNoDigitError(ValidationError):
    """Ошибка: в пароле нет цифр"""
    def __init__(self):
        self.message = "Пароль должен содержать хотя бы одну цифру"
        super().__init__(self.message)

class PasswordNoSpecialCharError(ValidationError):
    """Ошибка: в пароле нет специальных символов"""
    def __init__(self):
        self.message = "Пароль должен содержать хотя бы один специальный символ"
        super().__init__(self.message)

class UserAlreadyExistsError(ValidationError):
    """Ошибка: пользователь уже существует"""
    def __init__(self):
        self.message = "Пользователь с таким именем уже существует"
        super().__init__(self.message)
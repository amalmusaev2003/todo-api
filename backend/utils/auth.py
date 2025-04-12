import re
from exceptions import EmptyUsernameError, PasswordTooShortError, PasswordNoUppercaseError, PasswordNoLowercaseError, PasswordNoDigitError, PasswordNoSpecialCharError


# Проверка валидности имени пользователя
def validate_username(username: str):
    if not username or not username.strip():
        raise EmptyUsernameError()
    return username

# Проверка надежности пароля
def validate_password(password: str):
    """
    Проверяет, что пароль соответствует требованиям безопасности.
    Вызывает соответствующее исключение при нарушении требований.
    """
    if len(password) < 8:
        raise PasswordTooShortError()
    
    if not re.search(r'[A-Z]', password):
        raise PasswordNoUppercaseError()
        
    if not re.search(r'[a-z]', password):
        raise PasswordNoLowercaseError()
        
    if not re.search(r'\d', password):
        raise PasswordNoDigitError()
        
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise PasswordNoSpecialCharError()
        
    return password
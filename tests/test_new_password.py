import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
        
def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    password_length = 12
    password = generate_password(password_length)
    assert len(password) == password_length, f"Длина пароля {len(password)} не совпадает с ожидаемой {password_length}"



def test_empty_password():
    """Тест, что при генерации пароля длины 0 возвращается пустая строка"""
    password = generate_password(0)
    assert password == "", "Пароль не пустой"
"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
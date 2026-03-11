from dataclasses import dataclass


@dataclass
class User:
    name: str
    phone: str
    email: str


test_user = User(
    name="Artur",
    phone='+79217392590',
    email='arturoleynik@yandex.ru'
)

test_user_with_invalid_name = User(
    name='',
    phone='+79217392590',
    email='arturoleynik@yandex.ru'
)

test_user_with_invalid_phone = User(
    name='Artur',
    phone='+7921',
    email='arturoleynik@yandex.ru'
)

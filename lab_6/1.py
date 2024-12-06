class UserAccount:
    username = 'example'
    email = 'example@example.com'
    password = 'Не скажу 0_0'

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return f'Вы успешно изменили пароль'

    def check_password(self, password):
        return True if self.__password == password else False

user_1 = UserAccount('admin', 'admin@admin', '2')
print(user_1.set_password('5'))
print(user_1.check_password('8'))
print(user_1.check_password('5'))
print(user_1.password)
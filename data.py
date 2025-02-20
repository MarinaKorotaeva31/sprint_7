class Data:
    # Данные, используемые для регистрации нового пользователя с последующим удалением аккаунта
    LOGIN = "ninja1614"
    PASSWORD = "654321"
    FIRST_NAME = "Ваня"
    # Словарь для создания заказа
    DATA_FOR_ORDERS = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
    # Тела ответов
    CODE_200 = '{"ok":true}'
    CODE_400 = "Недостаточно данных для создания учетной записи"
    CODE_400_login = "Недостаточно данных для входа"
    CODE_404 = "Учетная запись не найдена"
    CODE_409 = "Этот логин уже используется. Попробуйте другой."

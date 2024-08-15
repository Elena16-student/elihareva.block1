def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if '@' not in recipient and sender:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                break
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            break
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            break
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            break
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
            break


send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'puple@gmail.com', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', '1234@mail.ru', sender='1234@mail.ru')
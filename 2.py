def user_data(first_name, last_name, year_of_birth, city, e_mail, phone_number):
    print(
        f"Имя: {first_name}\nФамилия: {last_name}\n/"
        f"Год рождения: {year_of_birth}\nГород проживания: {city}/"
        f"\nE-mail: {e_mail}\nТелефон: {phone_number};")


user_data(first_name='Иван', last_name='Иванов', year_of_birth=2000, city='Иваново', e_mail='ivan@mail.ru',
          phone_number='+7(989)-765-43-21')
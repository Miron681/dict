meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'ЗАСКАМИТЬ': "Обмануть",
            "ХАЙП": "Что-то популярное"
            }
while True:
    word = input("Введите непонятное слово: ").upper()
    if word in meme_dict:
        print(meme_dict[word])
    elif word == 'ВЫХОД':
        break
    else:
        your_word=input("Вы неправильно ввели слово. Не хотите ли вы добавить его?").lower()
        if your_word in ['да', "хочу"]:
            val=input("Введите значение слова")
            meme_dict[word]=val

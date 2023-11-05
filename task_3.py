# TODO  Напишите функцию count_letters


def count_letters(text):
    letter_dict = {}
    text_list = list()
    # Составляет список всех букв
    for letter in text.lower():
        if letter.isalpha():
            text_list.append(letter)
    # Составляет словарь буква - кол-во букв
    for letter in text_list:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict):
    all_letters_quantity = sum(letter_dict.values())
    letter_frequency_dict = {}

    for letter in letter_dict:
        letter_frequency_dict[letter] \
            = f"{letter_dict[letter] / all_letters_quantity:.2f}"
    return letter_frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

for letter, frequency in calculate_frequency(count_letters(main_str)).items():
    print(f'{letter}: {frequency}')

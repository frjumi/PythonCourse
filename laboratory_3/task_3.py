def count_letters(text):
    lowercase_text = text.lower()
    symbol_list = []
    result_dict = {}

    for symbol in lowercase_text:
        if symbol.isalpha():
            symbol_list.append(symbol)

    for symbol in symbol_list:
        result_dict[symbol] = symbol_list.count(symbol)
    return result_dict


def calculate_frequency(symbol_dict):
    frequency_dict = {}
    values_list = list(symbol_dict.values())
    total_sum = 0

    for i in values_list:
        total_sum += i

    for item in symbol_dict.items():
        frequency_dict[item[0]] = item[1] / total_sum
    return frequency_dict


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

result = calculate_frequency(count_letters(main_str))
for index, item in result.items():
    print(f"{index}: {item:0.2f}")

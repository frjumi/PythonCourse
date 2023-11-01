def find_common_participants(participants_list_one, participants_list_two, separator=","):
    participants_list_one = participants_list_one.split(separator)
    participants_list_two = participants_list_two.split(separator)
    result = list(set(participants_list_one).intersection(set(participants_list_two)))
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(common_participants)

# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, divider_sign=','):
    first_group_set = set(first_group.split(divider_sign))
    second_group_set = set(second_group.split(divider_sign))
    intersection_set = first_group_set.intersection(second_group_set)
    sorted_list = sorted(list(intersection_set))
    return sorted_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой

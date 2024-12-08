from input_parser import take_input, day_one_column_splitting


def day_one_part_one():
    raw_input = take_input("input_day_one_part_one.txt")
    split_input = day_one_column_splitting(raw_input)
    left_column = split_input[0]
    right_column = split_input[1]
    difference_list = []

    while len(left_column) != 0  and len(right_column) != 0:
        smallest_number_left = left_column[0]
        smallest_number_right = right_column[0]
        for number_left in left_column:
            if number_left < smallest_number_left:
                smallest_number_left = number_left

        for number_right in right_column:
            if number_right < smallest_number_right:
                smallest_number_right = number_right
        difference = smallest_number_left - smallest_number_right
        if difference < 0:
           difference = difference * -1
        difference_list.append(difference)
        smallest_number_left_index = left_column.index(smallest_number_left)
        smallest_number_right_index = right_column.index(smallest_number_right)
        left_column.pop(smallest_number_left_index)
        right_column.pop(smallest_number_right_index)
    print(sum(difference_list))


def day_one_part_two():
    raw_input = take_input("input_day_one_part_one.txt")
    split_input = day_one_column_splitting(raw_input)
    left_column = split_input[0]
    right_column = split_input[1]
    occurrence_list = []
    for left_num in left_column:
        occurrence = right_column.count(left_num)
        occurrence_multiplied = left_num * occurrence
        occurrence_list.append(occurrence_multiplied)
    print(sum(occurrence_list))










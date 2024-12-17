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


def day_two_part_one():
    input_data = take_input("input_day_two.txt")
    safety_list = []

    for line_num, line in enumerate(input_data):
        safety_flag = 1   # if safe then 1 else 0
        line = line.split(" ")
        base_level = int(line[0])
        inc_or_dec = base_level - int(line[1])

        if inc_or_dec < 0:
            movement_change_flag = "inc"
        elif inc_or_dec > 0:
            movement_change_flag = "dec"
        else:
            safety_flag = 0
            safety_list.append(safety_flag)

        for level in line[1:len(line)]:
            level_int = int(level)
            threshold = base_level - level_int
            # logic to see if the movement of numbers are always increasing or decreasing or staying the same
            if threshold < 0:
                movement_type = "inc"
            elif threshold > 0:
                movement_type = "dec"
            else:
                movement_type = movement_change_flag
            # checks to see which way the movement was

            if movement_change_flag != movement_type or -3 > threshold or threshold > 3 or threshold == 0:
                    safety_flag = 0
                    break
            else:
                base_level = level_int

        safety_list.append(safety_flag)
    print(safety_list.count(1))



def day_two_part_two(input_data):
    safety_checker = 0
    for line in input_data:
        safety_flag = 1  # if safe then 1 else 0
        split_line = line.split(" ")
        values = []
        index_counter = 0
        dampener_value = 0
        split_line_length = len(split_line) - 1

        for level in range(split_line_length):
            level_int = int(split_line[level])
            threshold = int(split_line[level + 1]) - level_int
            values.append(threshold)
        if all([3 >= i >= 1 for i in values]) or all([-3 <= i <= -1 for i in values]):
            safety_checker += 1
        else:
            while index_counter != len(split_line):
                copy_values = []
                copy_split_lines = split_line.copy()
                copy_split_lines.pop(index_counter)
                for i in range(len(copy_split_lines) - 1):
                    copy_level_int = int(copy_split_lines[i])
                    diff = int(copy_split_lines[i + 1]) - copy_level_int
                    copy_values.append(diff)
                if all([3 >= i >= 1 for i in copy_values]) or all([-3 <= i <= -1 for i in copy_values]):
                    safety_checker += 1
                    index_counter = len(split_line)
                else:
                    index_counter += 1

    print(safety_checker)







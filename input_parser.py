def take_input(file_name):
    with open(file_name) as input_file:
        lines = input_file.read().splitlines()
        return lines


def day_one_column_splitting(input_list):
    """

    :param input_list: a list of input.
    :return: two lists of data split from the input list. The elements inside are of type int
    """
    column_left = []
    column_right = []
    for line in input_list:

        left_number = line.split("   ")[0]  # three spaces
        right_number = line.split("   ")[1]  # three spaces
        column_left.append(int(left_number))
        column_right.append(int(right_number))
    return column_left, column_right

def day_two_part_one():
    input_data = take_input("input_day_two.txt")
    safety_list = []

    for line in input_data:
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
            if movement_change_flag != movement_type:
                safety_flag = 0
                safety_list.append(safety_flag)
                break
            # checks to see if the movement is within the threshold of safety
            if -3 > threshold or threshold > 3 or threshold == 0:
                safety_flag = 0
                safety_list.append(safety_flag)
                break
            base_level = level_int

        safety_list.append(safety_flag)
    print(safety_list.count(1))




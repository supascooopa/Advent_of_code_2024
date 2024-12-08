def take_input(file_name):
    with open(file_name) as input_file:
        lines = input_file.readlines()
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


"""
File:         calculator.py
Author:       Vu Nguyen
Date:         11/22/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs take in a file contain the command
              for adding, multiplying, and displaying variable
              with it's variable name and value.
"""

CREATE = 'create'
ADD = 'add'
DISPLAY = 'display'
MULTIPLY = 'mul'
ALL = 'all'


class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def already_made(variable_name, var_list):
    """
    The goal of this helper function is to checks if the
    variable was already exist.
    :param variable_name: the name of the variable
    :param var_list: the list of all variable object
    :return: available_var
    """
    available_var = None
    for var in var_list: # <-- Loops through all variable object
        if var.name == variable_name:
            available_var = var

    if not available_var:
        return available_var
    else:
        return available_var


def create(comm, var_list):
    """
    This functions create either new variable or change
    the old variable.
    :param comm: the command that also contain variable name and value
    :param var_list: the list of variable object
    :return: update the list with new variable object or it's value
    """
    # create format: (0-Command, 1-Variable Name, 2-Variable Value)

    check_var = already_made(comm[1], var_list)
    if not check_var:
        var_list.append(Variable(comm[1], comm[-1]))
    else:
        check_var.value = comm[-1]


def add(comm, var_list):
    # add format: (0-Command, 1-First Value, 2-Second Value, 3-Sum of first and second value)
    first_value = None
    second_value = None

    for var in var_list:

        # This condition checks for the repeated sum of two variable.
        if var.name == comm[1] and var.name == comm[2]:
            first_value = var.value
            second_value = var.value
        else:
            if var.name == comm[1]:
                first_value = var.value
            elif var.name == comm[2]:
                second_value = var.value

    the_sum = int(first_value) + int(second_value)
    check_var = already_made(comm[-1], var_list)

    if not check_var:
        var_list.append(Variable(comm[-1], str(the_sum)))
    else:
        check_var.value = str(the_sum)


def multiply(comm, var_list):
    # Multiplication format: (0-Command, 1-First Value, 2-Second Value, 3-Sum of first and second value)
    first_value = None
    second_value = None

    for var in var_list:

        # This condition checks for repeated product variable.
        if var.name == comm[1] and var.name == comm[2]:
            first_value = var.value
            second_value = var.value
        else:
            if var.name == comm[1]:
                first_value = var.value
            elif var.name == comm[2]:
                second_value = var.value

    the_product = int(first_value) * int(second_value)
    check_var = already_made(comm[-1], var_list)

    if not check_var:
        var_list.append(Variable(comm[-1], str(the_product)))
    else:
        check_var.value = str(the_product)


def display(comm, var_list):
    # Display format: (0-Command, 1-Variable/all)
    # This condition checks for individual variable display or all the variable display
    if comm[-1] == ALL:
        for var in var_list:
            print(var.name, var.value)
    else:
        for var in var_list:
            if var.name == comm[-1]:
                print(var.name, var.value)


if __name__ == "__main__":
    file_reader = open(input("What file do you wish to run? "), 'r')
    variable_list = []

    for line in file_reader.readlines():
        command = line.split()  # <-- This is a list of command (line by line)

        if command[0] == CREATE:  # <-- This checks for create command
            create(command, variable_list)

        elif command[0] == ADD:  # <-- This checks for add command
            add(command, variable_list)

        elif command[0] == MULTIPLY:  # <-- This checks for mul command
            multiply(command, variable_list)

        else:  # <-- This checks for display command
            display(command, variable_list)

    file_reader.close()

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    for problem in problems:
        problem_array = problem.split(" ")
        first_operand = problem_array[0]
        operator = problem_array[1]
        second_operand = problem_array[2]
        result = ''
        longest_number_length = len(max([first_operand, second_operand, result], key = len))
        dashes_length = longest_number_length + 2
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == '+':
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))
        first_line += (' ' * (dashes_length - len(first_operand))) + first_operand + '    '
        second_line += operator + ' ' + (' ' * (longest_number_length - len(second_operand))) + second_operand + '    '
        third_line += ('-' * dashes_length) + ('    ')
        fourth_line += (' ' * (dashes_length - len(result))) + result + '    '
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()
    if show_answers:
        return f'{first_line}\n{second_line}\n{third_line}\n{fourth_line}'
    return f'{first_line}\n{second_line}\n{third_line}'
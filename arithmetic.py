def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    third_line = ''
    second_line = ''
    for problem in problems:
        problem_array = problem.split(" ")
        first_operand = problem_array[0]
        operator = problem_array[1]
        second_operand = problem_array[2]
        longest_operand_length = len(max(problem_array, key = len))
        dashes_length = longest_operand_length + 2
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        third_line += ('-' * dashes_length) + ('    ')
        second_line += operator + ' ' + (' ' * (longest_operand_length - len(second_operand))) + second_operand + '    '
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    return problems
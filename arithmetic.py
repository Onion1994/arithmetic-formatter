def arithmetic_arranger(problems, show_answers=False):
    for problem in problems:
        problem_array = problem.split(" ")
        first_operand = problem_array[0]
        operator = problem_array[1]
        second_operand = problem_array[2]
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
    return problems
def arithmetic_arranger(problems, show_answers=False):
    for problem in problems:
        problem_array = problem.split(" ")
        if problem_array[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
    return problems
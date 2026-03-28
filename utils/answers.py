def validate_answers(answers: str) -> tuple[list, list]:
    answers = answers.split("\n")
    correct_answers = []
    errors = []

    for answer in answers:
        correct_answer = ".".join(answer.split(".")[1:])
        if correct_answer:
            correct_answers.append(correct_answer.strip())
        else:
            errors.append(answer)

    return correct_answers, errors

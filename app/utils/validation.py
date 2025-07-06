from .exceptions import ValidationError


def validate_qa_payload(data: dict) -> tuple[str, str]:
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a JSON object")

    question = data.get("question", "")
    answer = data.get("answer", "")

    if not question or not answer:
        raise ValidationError("Question and Answer are required fields")
    if len(question) > 100:
        raise ValidationError("Question must be 100 characters or fewer")
    if len(answer) > 500:
        raise ValidationError("Answer must be 500 characters or fewer")

    return question, answer


def validate_and_normalise_question_param(question_param: str) -> str:
    if question_param is None:
        raise ValidationError("Question parameter is required")
    if not isinstance(question_param, str):
        raise ValidationError("Question must be a string")

    question = question_param.strip().lower()

    if not question:
        raise ValidationError("Question cannot be empty")
    if len(question) > 100:
        raise ValidationError("Question must be 100 characters or fewer")

    return question

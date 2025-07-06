from .models import QAPair
from .repository import store_qa, fetch_answer, list_questions, mark_qa_deleted


def add_qa_pair(question: str, answer: str) -> dict:
    qa = QAPair(question, answer)

    if fetch_answer(qa.question):
        raise ValueError("Duplicate question.")

    store_qa(qa)
    return qa.to_dict()


def get_answer_by_question(question: str) -> str | None:
    return fetch_answer(question)


def get_all_questions() -> list[str]:
    return list_questions()


def soft_delete_qa_pair(question: str) -> bool:
    return mark_qa_deleted(question)

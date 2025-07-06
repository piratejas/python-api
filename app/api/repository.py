from .models import QAPair

_qa_store: dict[str, QAPair] = {}


def store_qa(qa: QAPair):
    _qa_store[qa.question] = qa


def fetch_answer(question: str) -> str | None:
    qa = _qa_store.get(question)
    if qa and not qa.is_deleted:
        return qa.answer
    return None


def list_questions(limit=10) -> list[str]:
    return [q for q, qa in _qa_store.items() if not qa.is_deleted][:limit]


def mark_qa_deleted(question: str) -> bool:
    qa = _qa_store.get(question)
    if not qa:
        return False
    qa.soft_delete()
    return True

qa_data = {}

def add_qa_pair(question: str, answer: str) -> bool:
    key = question.strip().lower()
    if key in qa_data:
        return False
    qa_data[key] = answer.strip()
    return True

def get_answer(question: str) -> str | None:
    return qa_data.get(question.strip().lower())

def get_questions(limit: int = 10) -> list[str]:
    return list(qa_data.keys())[:limit]
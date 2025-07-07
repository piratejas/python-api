from datetime import datetime, timezone


class QAPair:
    def __init__(self, question: str, answer: str, is_deleted: bool = False):
        self.question = question.strip().lower()
        self.answer = answer.strip()
        self.is_deleted = is_deleted
        self.last_modified = (
            datetime.now(timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z")
        )

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "is_deleted": self.is_deleted,
            "last_modified": self.last_modified,
        }

    def soft_delete(self):
        self.is_deleted = True
        self.last_modified = (
            datetime.now(timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z")
        )

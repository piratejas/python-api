import pytest
from app.utils.validation import (
    validate_qa_payload,
    validate_and_normalise_question_param,
)
from app.utils.exceptions import ValidationError


class TestValidateQAPayload:
    def test_valid_payload(self):
        data = {"question": "What is the question?", "answer": "This is the answer."}
        question, answer = validate_qa_payload(data)
        assert question == "What is the question?"
        assert answer == "This is the answer."

    def test_missing_question(self):
        with pytest.raises(
            ValidationError, match="Question and Answer are required fields"
        ):
            validate_qa_payload({"answer": "This is the answer."})

    def test_missing_answer(self):
        with pytest.raises(
            ValidationError, match="Question and Answer are required fields"
        ):
            validate_qa_payload({"question": "This is the answer."})

    def test_question_too_long(self):
        q = "x" * 101
        with pytest.raises(
            ValidationError, match="Question must be 100 characters or fewer"
        ):
            validate_qa_payload({"question": q, "answer": "This is the answer."})

    def test_answer_too_long(self):
        a = "y" * 501
        with pytest.raises(
            ValidationError, match="Answer must be 500 characters or fewer"
        ):
            validate_qa_payload({"question": "What is the question?", "answer": a})

    def test_non_dict_input(self):
        with pytest.raises(ValidationError, match="Payload must be a JSON object"):
            validate_qa_payload("not a dict")


class TestValidateAndNormaliseQuestionParam:
    def test_valid_question_param(self):
        raw = "  WHAT IS THE QUESTION? "
        result = validate_and_normalise_question_param(raw)
        assert result == "what is the question?"

    def test_none_input(self):
        with pytest.raises(ValidationError, match="Question parameter is required"):
            validate_and_normalise_question_param(None)

    def test_not_a_string(self):
        with pytest.raises(ValidationError, match="Question must be a string"):
            validate_and_normalise_question_param(123)

    def test_empty_string(self):
        with pytest.raises(ValidationError, match="Question cannot be empty"):
            validate_and_normalise_question_param("   ")

    def test_question_too_long(self):
        long_q = "q" * 101
        with pytest.raises(
            ValidationError, match="Question must be 100 characters or fewer"
        ):
            validate_and_normalise_question_param(long_q)

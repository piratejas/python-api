from flask import jsonify
from .service import (
    add_qa_pair,
    get_answer_by_question,
    get_all_questions,
    soft_delete_qa_pair,
)
from ..utils.exceptions import ValidationError
from ..utils.validation import (
    validate_qa_payload,
    validate_and_normalise_question_param,
)


def handle_create_qa(data: dict):
    try:
        question, answer = validate_qa_payload(data)
        result = add_qa_pair(question, answer)
        return jsonify(result), 201
    except ValidationError as e:
        return jsonify({"error": e.message}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


def handle_get_answer(question_param: str):
    try:
        validate_and_normalise_question_param(question_param)
        answer = get_answer_by_question(question_param)
        if not answer:
            return jsonify({"error": "Question not found"}), 404
        return jsonify({"answer": answer}), 200
    except ValidationError as e:
        return jsonify({"error": e.message}), 400
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


def handle_list_questions():
    try:
        result = get_all_questions()
        return jsonify({"questions": result}), 200
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


def handle_delete_qa(question_param: str):
    try:
        validate_and_normalise_question_param(question_param)
        soft_delete_qa_pair(question_param)
        return jsonify({"message": "QA pair has been deleted"}), 200
    except ValidationError as e:
        return jsonify({"error": e.message}), 400
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception:
        return jsonify({"error": "Internal server error"}), 500

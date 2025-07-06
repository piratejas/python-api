from flask import request
from . import api
from .controller import (
    handle_create_qa,
    handle_get_answer,
    handle_list_questions,
    handle_delete_qa,
)


@api.route("/qa-pairs", methods=["POST"])
def create_qa():
    return handle_create_qa(request.get_json())


@api.route("/qa-pairs", methods=["DELETE"])
def delete_qa():
    question = request.args.get("question").strip().lower()
    return handle_delete_qa(question)


@api.route("/questions", methods=["GET"])
def list_questions():
    return handle_list_questions()


@api.route("/answers", methods=["GET"])
def get_answer():
    question = request.args.get("question").strip().lower()
    return handle_get_answer(question)

from flask import Blueprint, request, jsonify
from app.db import add_qa_pair, get_answer, get_questions

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/qa-pairs', methods=['POST'])
def create_qa():
    data = request.get_json()
    question = data.get("question")
    answer = data.get("answer")

    if not question or not answer:
        return jsonify({"error": "Question and answer are required."}), 400

    success = add_qa_pair(question, answer)
    if not success:
        return jsonify({"error": "Question already exists."}), 400

    return jsonify({"message": "QA pair added successfully."}), 201

@api.route('/questions', methods=['GET'])
def get_all_questions():
    questions = get_questions()
    return jsonify({"questions": questions})

@api.route('/answers', methods=["GET"])
def get_answer_by_question():
    question = request.args.get('question', '').strip().lower()
    if not question:
        return jsonify({"error": "Missing 'question' query param."}), 400
    answer = get_answer(question)
    if answer:
        return jsonify({"question": question, "answer": answer})
    return jsonify({"error": "Question not found."}), 404
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestAPI:
    def test_create_qa_success(self, client):
        res = client.post(
            "/api/qa-pairs",
            json={
                "question": "What is the question?",
                "answer": "This is the answer.",
            },
        )
        assert res.status_code == 201
        assert res.get_json()["question"] == "what is the question?"

    def test_create_qa_missing_fields(self, client):
        res = client.post("/api/qa-pairs", json={"question": "Only question"})
        assert res.status_code == 400
        assert "error" in res.get_json()

    def test_get_answer_success(self, client):
        client.post(
            "/api/qa-pairs",
            json={"question": "What is the question?", "answer": "This is the answer."},
        )
        res = client.get("/api/answers?question=What%20is%20the%20question?")
        assert res.status_code == 200
        assert res.get_json()["answer"] == "This is the answer."

    def test_get_answer_not_found(self, client):
        res = client.get("/api/answers?question=Unknown%20question")
        assert res.status_code == 404

    def test_list_questions(self, client):
        for i in range(3):
            client.post("/api/qa-pairs", json={"question": f"Q{i}", "answer": f"A{i}"})
        res = client.get("/api/questions")
        assert res.status_code == 200
        data = res.get_json()
        assert "questions" in data
        assert len(data["questions"]) >= 3

    def test_delete_qa_success(self, client):
        client.post(
            "/api/qa-pairs", json={"question": "Is this deleted?", "answer": "Yes"}
        )
        res = client.delete("/api/qa-pairs?question=Is%20this%20deleted?")
        assert res.status_code == 200
        assert "message" in res.get_json()

    def test_delete_qa_not_found(self, client):
        res = client.delete("/api/qa-pairs?question=Unknown")
        assert res.status_code == 404

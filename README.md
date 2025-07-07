# QA Chatbot API MVP

A lightweight Flask API for managing Question & Answer pairs.


## Features

- Add Q&A pairs
- List stored questions (up to 10)
- Retrieve answers by question
- Soft-delete Q&A pairs
- Case-insensitive and normalized matching
- Input validation and error handling
- Modular architecture: scalable and easy to test

---

## Requirements

- Python **3.10+**
- Makefile (recommended)

---

## Setup Instructions

1. **Clone the repo**

	```bash
	git clone https://github.com/piratejas/python-api.git
	cd python-api
    ```

2. **Run the app**

	```bash
	make run
	```

	This creates a virtual environment, installs all requirements and starts the application.

	The Flask app will be available at http://127.0.0.1:5000/

---

## API Endpoints

**POST /api/qa-pairs**

Create a new Q&A pair.

- Example request body:
	```json
	{
 		"question": "Is this a question?",
  		"answer": "Yes, it certainly is."
	}
	```

- Validation:
	- question: max 100 characters
	- answer: max 500 characters
	- duplicate questions are not permitted


**GET /api/questions**

Retrieve a list of stored questions (up to 10).
- Soft-deleted questions are excluded.
- Returns an empty list if no questions are found.


**GET /api/answers?question=...**

Returns the answer to a matching question.
- Matching is case-insensitive and whitespace-normalised
- Returns 404 if not found or deleted


**DELETE /api/qa-pairs?question?=...**

Marks a Q&A pair as deleted (soft-delete).
- Idempotent
- Returns 404 if question does not exist


---

## Project Structure

	app/
	├── api/
	│   ├── routes.py       	# HTTP endpoints (Flask)
	│   └── controller.py   	# Request orchestration, validation, error mapping
	├── service.py				# Business logic
	├── repository.py			# Data layer (in-memory store)
	├── models.py 				# Domain model (QAPair)
	├── utils/
	│   ├── validation.py   	# Input validation helpers
	│   └── exceptions.py   	# Custom exceptions (e.g., ValidationError)
	├── __init__.py         	# App factory
	└── run.py					# Entry point


---

## Testing

Run all tests with coverage report:

```bash
make test
```

This includes:
- Unit tests for validation
- Endpoint tests using *Flask* test client and *pytest* fixtures
- Coverage of success & failure paths


---

## Code Quality

Linting with *pylint* and formatting with *black*:

```bash
make format
make lint
```

## Future Improvements

- Integrate persistent storage (currently in-memory)
- Improve question search functionality (eg. fuzzy search, keyword search or AI integration)
- Swagger / OpenAI documentation
- Authentication middleware (eg. JWT)
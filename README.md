# 🔁 **Flask Echo Server**

A lightweight, production-ready Echo Server built with Flask, Pydantic v2, and Redis. It receives GET and POST requests,
validates input using Pydantic, tracks request count using Redis, and echoes back the data.

---

## 🚀 Features

- Echoes request data via GET or POST
- Request counter using Redis
- Input validation with Pydantic v2
- Accepts JSON, form-data, or query strings
- Docker support for easy deployment

---

## 📦 Requirements

- Python 3.10+
- Redis (local or remote)
- `pip` or `poetry` for dependency management

---

## 📥 Installation

Clone this repository or copy the single-file server code.
Then install the dependencies:

```bash
pip install flask redis pydantic
```

By default, the app runs on http://localhost:5000.

## 🧪 Example Requests


### ✅ Form Data

```bash
curl -X POST http://localhost:5000/echo -F "name=Alice" -F "age=30"
```

### ✅ JSON 

```bash
curl -X POST http://localhost:5000/echo -H "Content-Type: application/json" -d '{"name": "Alice", "age": 30}'
```

## Response
```json
{
    "echo": {
        "my name": "Anna"
    },
    "request_number": 5
}
```

### 📄 License

MIT License. Feel free to use, modify, and distribute this project with attribution.
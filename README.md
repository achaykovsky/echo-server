# 🔁 Flask Echo Server

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

- Python 3.9+
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

### ✅ GET (via browser or curl)

```bash
http://localhost:5000/echo?name=Alice&age=30
```

### ✅ POST (via browser or curl)

```bash
curl -X POST http://localhost:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice", "age": 30}'
```

### ✅ Form Data (via browser or curl)

```bash
curl -X POST http://localhost:5000/echo \
     -F "name=Alice" \
     -F "age=30"
```

### ✅ JSON (via browser or curl)

```bash
curl -X POST http://localhost:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice", "age": 30}'
```

### 🧯 Troubleshooting

**Redis errors (e.g. connection refused):**
Ensure Redis is running on localhost:6379 or set custom values using REDIS_HOST and REDIS_PORT environment variables.

**Docker error on Windows:**
If you get open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified., ensure Docker Desktop is
running.

**Flask not starting:**
Check that no other process is using port 5000, or change the port in app.py.

**Invalid JSON payload:**
Confirm the JSON body is valid and Content-Type header is set correctly to application/json.

### 📄 License

MIT License. Feel free to use, modify, and distribute this project with attribution.
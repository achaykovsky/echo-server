# Flask Echo Server

A simple, thread-safe Flask-based web server that provides an `/echo` endpoint for testing and debugging purposes.

## 📦 Features

- Accepts `POST` requests with either JSON or form data
- Thread-safe request counting
- Logs each request with timestamp and request number
- Echoes received data in the response

## 🛠 Requirements

- Python 3.10+
- Flask

## 🚀 Installation

### Using Poetry

```bash
poetry install


```bash
pip install flask
```

By default, the app runs on http://localhost:5000.

## 🧪 Example Requests

### ✅ GET (via browser or curl)

```bash
http://localhost:5000/echo?name=Alice&age=30
```

### 📡 Usage

POST/echo

Request Headers
*Content-Type: application/json

*Content-Type: application/x-www-form-urlencoded

Request Body (Examples)

### ✅ JSON

```json
{
  "name": "Alice",
  "age": 30
}
```

### ✅ Form Data:

```bash
name=Alice&age=30
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

### 📜 Logging

Each request is logged to stdout in the following format:

2025-05-23 12:00:00 [INFO] Request #1 | Data: {'message': 'Hello'}

### 📄 License

MIT License. Feel free to use, modify, and distribute this project with attribution.
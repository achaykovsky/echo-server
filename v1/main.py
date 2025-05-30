from flask import Flask, request, jsonify
import logging
import threading

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

request_count = 0
lock = threading.Lock()


@app.route("/echo", methods=["POST"])
def echo():
    global request_count

    with lock:
        request_count += 1
        count = request_count

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    logging.info(f"Request #{count} | Data: {data}")
    response = {
        "request_number": count,
        "echo": data
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

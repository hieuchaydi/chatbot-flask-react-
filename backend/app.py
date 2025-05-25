from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # ✅ Thêm dòng này
from inference import chat_with_bot  # giả sử đã có sẵn

app = Flask(__name__, static_folder="../frontend/build", template_folder="../frontend/build")
CORS(app)  # ✅ Bật CORS toàn cục (cho phép frontend gọi đến backend)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])  # ✅ Đã đúng method
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    response = chat_with_bot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

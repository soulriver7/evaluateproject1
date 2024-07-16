from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API 키와 모델 ID 설정
api_key = 'AIzaSyAWPPgcfMAleTKSEbmefamVsEoFDOi8qlM'  # 여기에 실제 API 키를 입력하세요
model_id = 'gemini-pro'

def generate_evaluation(student_info, desired_path):
    request_body = {
        "contents": [{
            "parts": [{
                "text": f"학생 이름: {student_info['name']}\n성격: {student_info['personality']}\n취미: {student_info['hobbies']}\n특기: {student_info['specialties']}\n수상경력: {student_info['awards']}\n원하는 진로: {desired_path}\n\n해당 학생은 {desired_path}을 목표로 합니다. 이 학생의 강점과 약점을 분석하고, {desired_path}에 도움이 되는 구체적인 평가내역을 작성해주세요."
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 0.9,
            "topK": 40,
            "maxOutputTokens": 1024,
        },
    }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent"
    
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json=request_body
    )

    if response.status_code == 200:
        generated_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return generated_text
    else:
        raise Exception(f"API 요청 오류: {response.status_code}, {response.text}")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate_evaluation", methods=["POST"])
def generate_evaluation_api():
    data = request.get_json()
    student_info = data["studentInfo"]
    desired_path = data["desiredPath"]

    try:
        evaluation_text = generate_evaluation(student_info, desired_path)
        response = {"evaluation": evaluation_text}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
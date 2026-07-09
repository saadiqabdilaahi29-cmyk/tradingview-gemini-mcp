import os
from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Waxaan isticmaaleynaa API_KEY iyo WEBHOOK_SECRET oo aan ka soo qaadaneyno Render Environment
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Xaqiijinta Secret-ka si aanad u helin codsiyo aan la oggolayn
    if request.headers.get('X-Webhook-Secret') != WEBHOOK_SECRET:
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.json
    try:
        # Isticmaalka qaabka cusub ee Google GenAI
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=str(data)
        )
        return jsonify({"status": "success", "response": response.text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    

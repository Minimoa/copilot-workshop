from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

app = Flask(__name__)

client = AzureOpenAI(
  azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),
  api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")
)

@app.route('/')
def _index():
  return render_template('index.html')

@app.route('/send', methods=['POST'])
def _send():
  user_input = request.json.get('message', '')
  
  try:
    response = client.chat.completions.create(
      model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
      messages=[{"role": "user", "content": user_input}]
    )
    result = response.choices[0].message.content
    return jsonify({'response': result})
  except Exception as e:
    return jsonify({'response': f'오류 발생: {str(e)}'}), 500

@app.route('/speech-token', methods=['GET'])
def _get_speech_token():
  return jsonify({
    'key': os.getenv("AZURE_SPEECH_KEY"),
    'region': os.getenv("AZURE_SPEECH_REGION")
  })

if __name__ == '__main__':
  app.run(debug=True)
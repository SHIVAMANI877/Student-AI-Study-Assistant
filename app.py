from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure with your Gemini API key (get from: https://ai.google.dev/)
API_KEY = 'AIzaSyBRf_L-wq6DcKFRXjSJaje0OMhqTNUQUOI'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-2.0-flash-001')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        question = data['question']
        
        # Generate response using Gemini
        response = model.generate_content(f"""
        You are an AI teaching assistant. Help the student with this query:
        {question}
        
        Provide a clear, structured response with examples if needed.
        Keep explanations under 500 words.
        """)
        
        return jsonify({'answer': response.text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
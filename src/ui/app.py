from flask import Flask, render_template, request, jsonify, session
import os
import sys
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extraction.pdf_extractor import PDFExtractor
from extraction.image_extractor import ImageExtractor
from extraction.text_extractor import TextExtractor
from models.llm_interface import LLMInterface

app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))
app.secret_key = 'patient_buddy_secret_key'  # For session management

pdf_extractor = PDFExtractor()
image_extractor = ImageExtractor()
text_extractor = TextExtractor()
llm = LLMInterface()

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp:
            file.save(temp.name)
            file_path = temp.name
        
        try:
            file_ext = os.path.splitext(file.filename)[1].lower()
            
            if file_ext == '.pdf':
                parameters = pdf_extractor.extract(file_path)
            elif file_ext in ['.png', '.jpg', '.jpeg']:
                parameters = image_extractor.extract(file_path)
            elif file_ext == '.txt':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                parameters = text_extractor.extract(text)
            
            session['parameters'] = parameters
            
            os.unlink(file_path)
            
            return jsonify({
                'success': True,
                'parameters': parameters
            })
        except Exception as e:
            os.unlink(file_path)
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle questions about the extracted parameters"""
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400
    
    question = data['question']
    
    parameters = session.get('parameters', {})
    
    answer = llm.get_answer(question, parameters)
    
    return jsonify({
        'success': True,
        'answer': answer
    })

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.dirname(__file__), 'templates'), exist_ok=True)
    app.run(debug=True)
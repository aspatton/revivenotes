from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

def format_notes(raw_notes):
    """Format raw notes into professional format"""
    formatted = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'content': '\n'.join(line for line in raw_notes.split('\n') if line.strip()),
    }
    return formatted

def generate_homework():
    """Generate homework assignments based on common therapeutic practices"""
    return [
        'Practice mindfulness exercises for 10 minutes daily',
        'Complete mood tracking journal',
        'Practice deep breathing exercises when feeling anxious'
    ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/format_notes', methods=['POST'])
def process_notes():
    raw_notes = request.json.get('notes', '')
    if not raw_notes:
        return jsonify({'error': 'No notes provided'}), 400
    
    formatted = format_notes(raw_notes)
    homework = generate_homework()
    
    return jsonify({
        'formatted_notes': formatted,
        'homework': homework
    })

if __name__ == '__main__':
    app.run(debug=True)

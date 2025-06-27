# Simple Flask app - app_simple.py
import os
from flask import Flask, render_template, request

# Import the simple version instead of complex agents
from lang import process_pdf_question_simple

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        question = request.form['question']
        pdf_file = request.files['pdf']

        if pdf_file and pdf_file.filename.endswith(".pdf"):
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
            pdf_file.save(file_path)

            try:
                print(f"Processing question: {question}")
                print(f"Processing PDF: {pdf_file.filename}")
                
                # Use the simple processing function
                answer = process_pdf_question_simple(file_path, question)
                
                print(f"Final answer: {answer}")

            except Exception as e:
                answer = f"❌ Error: {str(e)}"
                print(f"Error occurred: {e}")
                import traceback
                traceback.print_exc()
            finally:
                # Clean up uploaded file
                if os.path.exists(file_path):
                    os.remove(file_path)
                    
                # Clean up chroma db
                import shutil
                if os.path.exists("./chroma_db"):
                    try:
                        shutil.rmtree("./chroma_db")
                    except:
                        pass
        else:
            answer = "⚠️ Please upload a valid PDF file."

    return render_template('index.html', response=answer)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# Route to serve the Gemba Walk UI
@app.route('/')
def gogemba():
    return render_template('GoGemba.html')

if __name__ == '__main__':
    app.run(debug=True)

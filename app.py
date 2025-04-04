from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        language = request.form['language']
        return render_template(
            'result.html',
            name=name,
            email=email,
            message=message,
            language=language
        )
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return render_template('result.html', name=name, message=message)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)

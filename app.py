from flask import (Flask, render_template,request)
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        dta = request.form.get('imgdata')
        return render_template(
            'index.html',
            dta = dta
        )
    else:
        return render_template(
            'index.html'
        )
    

if __name__ == '__main__':
    app.run(debug=True)



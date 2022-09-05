from flask import Flask, request, render_template

# Flask Constructor
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def gfg():
    if request.method == 'POST':
        codigo = request.form.get('fcodigo')
        return "CODIGO: " + codigo
    return render_template('form.html')

if __name__ == '__main__':
    app.run()

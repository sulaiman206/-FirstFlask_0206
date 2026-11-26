from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_nama = None
    hasil_nim = None

    if request.method == 'POST':
        # Parsing parameters dari form menggunakan method POST
        hasil_nama = request.form.get('nama')
        hasil_nim = request.form.get('nim')

    return render_template('index.html', nama=hasil_nama, nim=hasil_nim)

if __name__ == '__main__':
    app.run(debug=True)
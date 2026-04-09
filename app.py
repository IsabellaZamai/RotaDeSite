from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    return "Site fanclube do salsicha"

@app.route('/SalsichaDodia')
def Salsicha():
    return "Scooby-Doo:filme"

if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)
    
    app.run(host='0.0.0.0', port=8000)



from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/institution", methods=['GET'])
def institution():
    return render_template("institution.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'template'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

@app.route("/")
def main():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)
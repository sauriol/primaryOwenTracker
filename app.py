from flask import Flask, render_template


app = Flask(__name__, template_folder = '../primary_owen_tracker/primary_owen_tracker/templates')


@app.route("/")
def main():
    return "wht"

if __name__ == "__main__":
    app.run()

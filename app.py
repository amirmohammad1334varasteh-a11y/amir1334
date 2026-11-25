from flask import Flask, render_template, request

app = Flask(__name__)

text = "i am learning Arabic. i like it."
password = "amir1334varasteh"


@app.route("/", methods=["GET", "POST"])
def home():
    result1 = ""
    result2 = ""

    if request.method == "POST":
        c = request.form.get("password1", "")

        if c == password:
            result1 = text
        else:
            result1 = "all randooom"

        a = request.form.get("password2", "")

        if a == "amir1334varasteh and amir1334varasteh":
            result2 = "Arabic=english"
        else:
            result2 = "all random"

    return render_template(
        "index.html",
        result1=result1,
        result2=result2
    )


if __name__ == "__main__":
    app.run(debug=True)
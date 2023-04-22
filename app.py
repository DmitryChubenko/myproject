from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "id": 1,
        "text": "Який кольоровий простір використовується для відображення веб-сторінок?",
        "options": ["RGB", "CMYK", "Hex", "Lab"],
        "answer": "RGB"
    },
    {
        "id": 2,
        "text": "Який тег використовується для створення списку з номерованими елементами?",
        "options": ["<ul>", "<ol>", "<li>", "<dl>"],
        "answer": "<ol>"
    },
    {
        "id": 3,
        "text": "Який атрибут HTML використовується для зв'язування зовнішнього файла зі стилями?",
        "options": ["class", "id", "href", "src"],
        "answer": "href"
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        score = 0
        for question in questions:
            answer = request.form.get(str(question["id"]))
            if answer == question["answer"]:
                score += 1
        num_questions = len(questions)
        return render_template("test.html", score=score, num_questions=num_questions, questions=questions)
    else:
        return render_template("test.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)

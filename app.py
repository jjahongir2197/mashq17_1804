from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def sum_n():

    if request.method == "POST":

        n = int(request.form["n"])

        total = 0

        for i in range(1, n+1):
            total += i

        return f"Yig‘indi: {total}"

    return render_template("index.html")

app.run(debug=True)

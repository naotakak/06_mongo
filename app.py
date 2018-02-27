from flask import Flask, render_template, request
from utils import movies

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("base.html")

@app.route("/title", methods=["GET"])
def title():
    return render_template("get_result.html", typ = "Title", result = movies.search_title(request.args.get("input").replace("+", " ")))

@app.route("/after_year", methods=["GET", "POST"])
def after_year():
    return render_template("get_result.html", typ = "After year", result = movies.after_year(int(request.args.get("input"))))

@app.route("/director", methods=["GET"])
def director():
    return render_template("get_result.html", typ = "Director", result = movies.director(request.args.get("input").replace("+", " ")))

@app.route("/year", methods=["GET"])
def year():
    return render_template("get_result.html", typ = "Year", result = movies.year(int(request.args.get("input"))))

@app.route("/before_year", methods=["GET"])
def before_year():
    return render_template("get_result.html", typ = "Before year", result = movies.before_year(int(request.args.get("input"))))

@app.route("/genreyear", methods=["GET"])
def genreyear():
    return render_template("get_result.html", typ = "Genre + Year", result = movies.genre_year(request.args.get("genre").replace("+", " "), int(request.args.get("year"))))

if __name__ == "__main__":
   app.debug = True
   app.run()
   

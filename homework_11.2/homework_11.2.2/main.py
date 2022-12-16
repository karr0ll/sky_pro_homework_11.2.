from utils import load_json_candidates
from utils import get_candidate_by_id, get_candidate_by_name, get_candidate_by_skill
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start_page():

    """выводит начальную страницу"""

    data = load_json_candidates()
    return render_template("list.html", candidates=data)


@app.route("/candidate/<int:uid>")
def load_candidate_page(uid):

    """выводит профиль кандидата по id"""

    data = get_candidate_by_id(uid)
    return render_template("candidate_file.html", candidate=data)


@app.route("/search/<candidate_name>")
def search_candidate_by_name(candidate_name):

    """ищет кандидата по имени"""

    counter = 0
    data = get_candidate_by_name(candidate_name)
    for item in data:
        counter += 1
    return f"<h2>Найдено кандидатов: {counter}</h2>" + render_template("search.html", candidates=data)


@app.route("/skill/<candidate_skill>")
def search_candidate_by_skill(candidate_skill):

    """ищет кандидата по навыку"""

    data = get_candidate_by_skill(candidate_skill)
    counter = 0
    for item in data:
        counter += 1
    return f"<h2>Найдено кандидатов c навыком '{candidate_skill}': {counter}</h2>" + \
        render_template("skill.html", candidates=data)


app.run()

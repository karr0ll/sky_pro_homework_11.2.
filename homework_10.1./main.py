from flask import Flask
from utils import load_candidates, get_candidates_list

app = Flask(__name__)


@app.route("/")
def start_page():
    table = get_candidates_list()
    return table


@app.route("/candidate/<int:id_>")
def candidate_page(id_):
    candidates = load_candidates()
    profile = ""
    for candidate in candidates:
        if candidate["id"] == id_:
            profile += f"""<img src="{candidate["picture"]}">\n"""
            profile += "<pre>"
            profile += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}
            """
    profile += "</pre>"
    return profile


@app.route("/skill/<skill>")
def candidate_skill_page(skill):
    candidates = load_candidates()
    profile = ""
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower():
            profile += "<pre>"
            profile += f"""
                        {candidate["name"]}\n
                        {candidate["position"]}\n
                        {candidate["skills"]}
                        """
        profile += "</pre>"
    return profile


app.run()

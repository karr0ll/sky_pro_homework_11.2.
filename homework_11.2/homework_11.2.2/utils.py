import json
import os


def load_json_candidates():

    """загружает список кандидатов из файла json"""

    with open(os.path.join("candidates.json"), "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate_by_id(candidate_id):

    """выводит файл кандидата по id"""

    candidates = load_json_candidates()
    for item in candidates:
        if item["id"] == candidate_id:
            return item


def get_candidate_by_name(candidate_name):

    """загружает список кандидатов по имени"""

    candidates = load_json_candidates()
    candidates_name = []
    for item in candidates:
        if item["name"] == candidate_name:
            candidates_name.append(item)
            return candidates_name


def get_candidate_by_skill(candidate_skill):

    """выводит кандидата по навыку"""

    candidates = load_json_candidates()
    candidates_by_skills = []
    for item in candidates:
        if candidate_skill.lower() in item["skills"].lower().split(", "):
            candidates_by_skills.append(item)
            print(item["skills"].lower().split(", "))
    return candidates_by_skills

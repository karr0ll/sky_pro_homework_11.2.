import json
import os

def load_candidates():
    """загружает список данных кандидатов из файла json"""
    with open(os.path.join("candidates.json"), "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def get_candidates_list():
    """форматирует вывод списка всех кандидатов"""
    candidates: list[dict] = load_candidates()
    table = ""
    for candidate in candidates:
            table += "<pre>"
            table += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}
            """
    table += "</pre>"
    return table


def get_candidates_list():
    """форматирует вывод профиля кандидата"""
    candidates: list[dict] = load_candidates()
    table = "<pre>"
    for candidate in candidates:
            table += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}
            """
    table += "</pre>"
    return table




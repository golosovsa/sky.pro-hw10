"""
    Homevork №10
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/10-147f59fe4aed4309a7281304f61b7680

    Database singleton class
"""


class Candidate:
    def __init__(self, name, position, skills, picture):
        self._name = name
        self._position = position
        self._skills = skills
        self._skills_lower = skills.strip().lower().split(", ")
        self._picture = picture

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @property
    def skills(self):
        return self._skills

    @property
    def skills_lower(self):
        return self._skills_lower

    @property
    def picture(self):
        return self._picture

    def has_skill(self, skill):
        return skill.lower() in self._skills_lower

    @staticmethod
    def from_dict(record):
        undefined = "Undefined"
        name = record.get("name", undefined)
        position = record.get("position", undefined)
        skills = record.get("skills", undefined)
        picture = record.get("picture", undefined)
        return Candidate(name, position, skills, picture)

"""
    Homevork №10
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/10-147f59fe4aed4309a7281304f61b7680

    Database singleton class
"""
import json

from application.candidate import Candidate


class Database:
    """ Class database """
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Database, cls).__new__(cls)
            cls._db = dict()
        return cls._instance

    def __init__(self, source=None):
        if source is not None:
            self.connect(source)

    def connect(self, source):
        with open(source, "rt", encoding="utf-8") as fin:
            data = json.load(fin)

        for record in data:
            pk = record.get("id", None)
            if pk is None:
                raise RuntimeError("Primary key not found.")
            self._db[pk] = Candidate.from_dict(record)

    @property
    def count(self):
        return len(self._db)

    def select_all(self):
        return self._db.values()

    def select_by_pk(self, pk):
        return self._db.get(pk, None)

    def select_by_skill(self, skill):
        result = [candidate for pk, candidate in self._db.items() if candidate.has_skill(skill)]
        return result

    def select_pk_name(self):
        result = [(pk, candidate.name) for pk, candidate in self._db.items()]
        return result

    def select_skills(self):
        skills_uniq = set()
        for candidate in self._db.values():
            skills_uniq.update(set(candidate.skills_lower))
        return list(skills_uniq)

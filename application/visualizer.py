"""
    Homevork №10
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/10-147f59fe4aed4309a7281304f61b7680

    visualizer class
"""


import settings
from application.template import *
from application.database import Database


class Visualizer:
    _substitution = dict()

    def __init__(self):

        self.fill_default()

        self.fill_content()

        self.fill_id_links()
        self.fill_skill_links()

    @staticmethod
    def get_id_links(current=None):
        db = Database()
        pk_links = []
        for pk, name in db.select_pk_name():
            if current and pk == current:
                link = TEMPLATE_CURRENT_ID_LINK.format(candidate_id=pk, candidate_name=name)
            else:
                link = TEMPLATE_ID_LINK.format(candidate_id=pk, candidate_name=name)
            pk_links.append(link)
        return "\n".join(pk_links)

    @staticmethod
    def get_skill_links(current=None):
        db = Database()
        skill_links = []
        for skill in db.select_skills():
            if current and skill == current.lower():
                link = TEMPLATE_CURRENT_SKILL_LINK.format(skill=skill.capitalize())
            else:
                link = TEMPLATE_SKILL_LINK.format(skill=skill.capitalize())
            skill_links.append(link)

        return "\n".join(skill_links)

    def fill_default(self):
        db = Database()
        self._substitution["site_title"] = "Candidates - MAIN"
        self._substitution["app_version"] = settings.APP_VERSION
        self._substitution["count_db_records"] = str(db.count)
        self._substitution["view_name"] = "List of candidates:"

    def fill_content(self, *args, **kwargs):
        db = Database()
        content = []
        for candidate in db.select_all():
            record = f"{candidate.name}\n{candidate.position}\n{candidate.skills}\n"
            content.append(record)
        self._substitution["content"] = "\n".join(content)

    def fill_id_links(self, current=None):
        self._substitution["id_links"] = Visualizer.get_id_links(current)

    def fill_skill_links(self, current=None):
        self._substitution["skills_links"] = Visualizer.get_skill_links(current)

    def draw_template(self):
        return TEMPLATE_HTML.format(**self._substitution)


class VisualizerCandidate(Visualizer):

    def __init__(self, pk):
        self.fill_default()
        self.fill_content(pk=pk)
        self.fill_id_links(pk)
        self.fill_skill_links()

    def fill_content(self, *args, **kwargs):
        pk = kwargs.get("pk", "Undefined")
        db = Database()
        self._substitution["view_name"] = f"Candidate with id: {pk}"

        candidate = db.select_by_pk(pk)

        if candidate is None:
            self._substitution["content"] = "Candidate not found"
            return

        picture = TEMPLATE_CANDIDATE_PICTURE.format(candidate.picture)
        content = f"{picture}\n{candidate.name}\n{candidate.position}\n{candidate.skills}\n"
        self._substitution["content"] = content


class VisualizerSkill(Visualizer):

    def __init__(self, skill):
        self.fill_default()
        self.fill_content(skill=skill)
        self.fill_id_links()
        self.fill_skill_links(skill)

    def fill_content(self, *args, **kwargs):
        skill = kwargs.get("skill", "Undefined")
        db = Database()
        self._substitution["view_name"] = f"Candidates with skill: {skill}"

        content = []
        for candidate in db.select_by_skill(skill):
            record = f"{candidate.name}\n{candidate.position}\n{candidate.skills}\n"
            content.append(record)

        self._substitution["content"] = "\n".join(content) or "Candidates not found"

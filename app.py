"""
    Homework №10
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/10-147f59fe4aed4309a7281304f61b7680

    App file
"""

from flask import Flask

import settings
from application import database, visualizer

database.Database().connect(settings.APP_DATABASE)

app = Flask(__name__)


@app.route('/')
def route_main_page():
    main_page = visualizer.Visualizer()
    return main_page.draw_template()


@app.route('/candidate/<int:pk>/')
def route_candidate_page(pk):
    candidate_page = visualizer.VisualizerCandidate(pk)
    return candidate_page.draw_template()


@app.route('/skill/<skill>/')
def route_skill_page(skill):
    skill_page = visualizer.VisualizerSkill(skill)
    return skill_page.draw_template()


if __name__ == '__main__':
    app.run(debug=True)

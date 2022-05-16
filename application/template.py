"""
    Homevork №10
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/10-147f59fe4aed4309a7281304f61b7680

    Template file
"""


TEMPLATE_HTML = r"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_title}</title>
    <style>
        * {{
    margin: 0;
    padding: 0;
}}

.body {{
    font-family: Sans-serif;
    display: flex;
    flex-flow: column nowrap;
    height: 100vh;
    gap: 32px;
}}

.align {{
    padding-left: Max(calc(50vw - 600px), 32px);
    padding-right: Max(calc(50vw - 600px), 32px);
}}

.header {{
    flex: 0 0 auto;
    display: flex;
    gap: 32px;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: flex-start;
    justify-content: space-between;
    align-items: center;
    padding-top: 16px;
    padding-bottom: 16px;
    background-color: #888;
    color: #fff;
}}

.content {{
    flex: 1 0 auto;
    box-sizing: border-box;
}}

.content__header {{
    margin-bottom: 16px;
}}

.footer {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    border-top: 1px solid #888;
    flex: 0 0 auto;
    gap: 32px;
    padding-top: 16px;
    padding-bottom: 16px;
}}

.footer__item {{
    flex: 1 0 auto;
    display: flex;
    flex-flow: column nowrap;
    gap: 16px;
}}

.footer__menu {{
    display: flex;
    gap: 16px;
}}

.footer__menu_links {{
    flex-flow: column nowrap;
}}

.footer__menu_cards {{
    flex-flow: row wrap;
}}

.footer__link {{
    text-decoration: none;
    color: #888;
    transition: color 0.3s;
}}

.footer__link:hover {{
    color: black;
}}

.footer__link_current {{
    color: black;
}}

.footer__card {{
    box-sizing: border-box;
    padding-top: 0.3em;
    padding-bottom: 1.3em;
    height: 1.5em;
    padding-left: 1.5em;
    padding-right: 1.5em;
    border: 1px solid #333;
    background-color: #888;
    color: #fff;
    border-radius: 15px;
    max-width: 150px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-decoration: none;
    transition: color 0.3s;
}}

.footer__card:hover {{
    color: black;
}}

.footer__card_current {{
    color: black;
}}
    </style>
</head>
<body class="body">
    
    <header class="header align">
        <h1 class="header__title">Simple web app</h1>
        <p class="header__info">database contains {count_db_records} records</p>
        <p class="header__version">Version: {app_version}</p>
    </header>

    <section class="content align">
        <h2 class="content__header">{view_name}</h2>
        <pre class="content__pre">
{content}
        </pre>
    </section>

    <footer class="footer align">
        <div class="footer__item">
            <h2 class="footer__title">Candidates by ID</h2>
            <nav class="footer__menu footer__menu_links">
{id_links}
            </nav>
        </div>
        <div class="footer__item">
            <h2 class="footer__title">Skills</h2>
            <nav class="footer__menu footer__menu_cards">
{skills_links}
            </nav>
        </div>
    </footer>

</body>
</html>
"""

TEMPLATE_ID_LINK = '<a class="footer__link" href="/candidate/{candidate_id}/">' \
                   'ID: {candidate_id} Name: {candidate_name}' \
                   '</a>'

TEMPLATE_CURRENT_ID_LINK = '<a class="footer__link footer__link_current" href="/candidate/{candidate_id}/">' \
                           'ID: {candidate_id} Name: {candidate_name}' \
                           '</a>'

TEMPLATE_SKILL_LINK = '<a class="footer__card" href="/skill/{skill}/" title="{skill}" >' \
                      '{skill}' \
                      '</a>'

TEMPLATE_CURRENT_SKILL_LINK = '<a class="footer__card footer__card_current" href="/skill/{skill}/" title="{skill}" >' \
                      '{skill}' \
                      '</a>'

TEMPLATE_CANDIDATE_PICTURE = '<img class="content__img" src="{}" alt="Candidate picture" />'

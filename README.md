# Homework №10  
[link to the source](https://skyengpublic.notion.site/10-147f59fe4aed4309a7281304f61b7680)
### Task:
Create simple web app
## What should you do:  
### Step 0:  
Save data to candidates.json file
```json
[
  {
    "id": 1,
    "name": "Adela Hendricks",
    "picture": "https://picsum.photos/200",
    "position": "Go разработчик",
    "gender": "female",
    "age": 40,
    "skills": "go, python"
  },
  {
    "id": 2,
    "name": "Sheri Torres",
    "picture": "https://picsum.photos/200",
    "position": "Delphi developer",
    "gender": "female",
    "age": 26,
    "skills": "Delphi, pascal, fortran, basic"
  },
  {
    "id": 3,
    "name": "Burt Stein",
    "picture": "https://picsum.photos/200",
    "position": "Team lead",
    "gender": "male",
    "age": 33,
    "skills": "делегирование, пользоваться календарем, обсуждать важные вопросы"
  },
  {
    "id": 4,
    "name": "Bauer Adkins",
    "picture": "https://picsum.photos/200",
    "position": "CTO",
    "gender": "male",
    "age": 37,
    "skills": "very important face"
  },
  {
    "id": 5,
    "name": "Day Holloway",
    "picture": "https://picsum.photos/200",
    "position": "HR manager",
    "gender": "male",
    "age": 35,
    "skills": "LinkedIn, telegram, spam, spam, spam"
  },
  {
    "id": 6,
    "name": "Austin Cochran",
    "picture": "https://picsum.photos/200",
    "position": "python-develop",
    "gender": "male",
    "age": 26,
    "skills": "python, html"
  },
  {
    "id": 7,
    "name": "Sheree Love",
    "picture": "https://picsum.photos/200",
    "position": "Django developer",
    "gender": "female",
    "age": 33,
    "skills": "Python, Django, flask"
  }
]
```
Place file to your app directory
### Step 1:  
* Create a view for "/" route (for Main Page)
* Output the text in this format (use tag <pre> - preformatting)
```html
<pre>
  The name of the candidate -
  The position of the candidate
  Skills list through a comma

  The name of the candidate -
  The position of the candidate
  Skills list through a comma

  The name of the candidate -
  The position of the candidate
  Skills list through a comma
<pre>
```
### Step 2:  
* Create a view for "/candidates/<int:x>" route, this is must display the candidate's data (for example):
```html
<img src="(picture uri)">

<pre>
  The name of the candidate -
  The position of the candidate
  Skills list through a comma
</pre>
```

### Step 3:  
* Create a view for "/skills/<str:x>" route, output those candidates in the list of skills that contain "<x>"
```html
<pre>
  The name of the candidate -
  The position of the candidate
  Skills list through a comma

  The name of the candidate -
  The position of the candidate
  Skills list through a comma

  The name of the candidate -
  The position of the candidate
  Skills list through a comma
<pre>
```
## How it should be implemented  
### What will be checked in the homework:  
- [ ] Flask is installed and works
- [ ] The route without parameters is shown correctly
- [ ] The route with parameters is shown correctly
- [ ] When requesting `get/` a list of candidates is displayed
- [ ] When requesting `get /candidate/<x> `one candidate is displayed
- [ ] When requesting `get /skills/<x> `candidates with the skill are displayed
- [ ] Route-view parameter are independent of lower/upper register
 
 ## Project status
 ### Tag v1.0
 - Create MVP
![Art](https://i.postimg.cc/nrYBQjDB/art.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/Musical-Studying?style=flat&color=C8102E)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/Musical-Studying?style=flat&color=012169)
![Pet Project](https://img.shields.io/badge/pet-project-8400FF)

# Musical Studying&nbsp;&#127911;

A web service for learning English through songs. My first Django project&nbsp;&#128304;.

## Description

Users can listen to their favorite songs and do exercises to better learn grammar and vocabulary. There is a built-in song recommendation system based on the listener's preferences&nbsp;&#128156;.

Site sections:

- &#127775;&nbsp;Home (landing page with information about the benefits of this way of learning a language)
- &#127919;&nbsp;Daily selection of songs (based on favorite genres and chosen song difficulty)
- &#128451;&nbsp;Library of all available songs (with filtering by genre and difficulty)
- &#128270;&nbsp;Song study (ability to listen to a song, watch a music video, view lyrics and translation)
- &#128104;&#8205;&#127979;&nbsp;Exercises for the song (several automatically selected exercises that test the vocabulary and grammar used in the song)
- &#128221;&nbsp;Registration (fields for name, email, password, English level, and preferred music)
- &#128273;&nbsp;Authorization (fields for email and password)
- &#128100;&nbsp;Personal account (ability to change basic account settings)
- &#128271;&nbsp;Admin panel (administrators can add new songs and exercises)

## Technologies and tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white&color=013b2a)
![Aiohttp](https://img.shields.io/badge/aiohttp-%232C5bb4.svg?style=for-the-badge&logo=aiohttp&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/html-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=white&color=yellow)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white&color=#6CeA8C)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white&color=f14e32)

## Technical decisions made:

- Data storage using SQLite
- Modular application structure (`main`, `loginsys`, `songs`, `tasks`)
- Custom authentication system based on built-in components (`django.contrib.auth`)
- Built-in Django template engine with a common `templates` folder
- Working with external APIs:
    - Yandex Music (`yandex-music`) - to get data about songs, genres, and lyrics
    - Google Translate (`googletrans`) - for translating texts
    - An asynchronous library (`aiohttp`) is used to interact with them, which allows not to block the main thread when performing long network requests
- Serving static files from the root `static` folder is configured


## Getting started

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&color=F7F7F7&multiline=true&width=750&height=165&lines=%25+git+clone+https%3A%2F%2Fgithub.com%2Fid-andyyy%2FMusical-Studying.git;%25+cd+Musical-Studying;%25+pip+install+-r+requirements.txt;%25+python+manage.py+migrate;%25+python+manage.py+createsuperuser;%25+python+manage.py+runserver)](https://git.io/typing-svg)

```sh
git clone https://github.com/id-andyyy/Musical-Studying.git
cd Musical-Studying
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Feedback

I would appreciate it if you give a star&nbsp;&#11088;. If you find a bug or have suggestions for improvement,
use the [Issues](https://github.com/id-andyyy/Musical-Studying/issues) section.

Читать на [русском&nbsp;&#127479;&#127482;](README.md)

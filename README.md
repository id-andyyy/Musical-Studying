![Арт](https://i.postimg.cc/nrYBQjDB/art.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/Musical-Studying?style=flat&color=C8102E)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/Musical-Studying?style=flat&color=012169)
![Pet Project](https://img.shields.io/badge/pet-project-8400FF)

# Musical Studying&nbsp;&#127911;

Веб-сервис для изучения английского языка с помощью песен. Мой первый проект на Django&nbsp;&#128304;.

## Описание

Пользователи могут слушать любимые песни и выполнять упражнения для лучшего изучения грамматики и лексики. Встроена система рекомендации песен, которая основывается на предпочтениях слушателя&nbsp;&#128156;.

Разделы сайта:

- &#127775;&nbsp;Главная (лендинг с информацией о преимуществах такого способа изучения языка)
- &#127919;&nbsp;Ежедневная подборка песен (на основе любимых жанров и выбранной сложности песен)
- &#128451;&nbsp;Библиотека всех доступных песен (с фильтрацией по жанру и сложности)
- &#128270;&nbsp;Изучение песни (возможность прослушать песню, посмотреть видеоклип, текст песни и её перевод)
- &#128104;&#8205;&#127979;&nbsp;Упражнения к песне (несколько автоматически подобранных упражнений, проверяющих лексику и грамматику, используемые в песне)
- &#128221;&nbsp;Регистрация (поля для имени, электронной почты, пароля, уровня английского и предпочитаемой музыки)
- &#128273;&nbsp;Авторизация (поля для электронной почты и пароля)
- &#128100;&nbsp;Личный кабинет (возможность изменить основные настройки аккаунта)
- &#128271;&nbsp;Админ-панель (администраторы могут добавлять новые песни и упражнения)

## Технологии и инструменты

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

## Принятые технические решения:

- Хранение данных с помощью SQLite
- Модульная структура приложения (`main`, `loginsys`, `songs`, `tasks`)
- Кастомная система аутентификации, которая базируется на встроенных компонентах (`django.contrib.auth`)
- Встроенный шаблонизатор Django с общей папкой `templates`
- Работа с внещними API:
    - Yandex Music (`yandex-music`) - получение данных о песнях, жанрах и текстах
    - Google Translate (`googletrans`) - для перевода текстов
    - Для взаимодействия с ними используется асинхронная библиотека (`aiohttp`), что позволяет не блокировать основной поток при выполнении долгих сетевых запросов
- Настроена раздача статических файлов из корневой папки `static`


## Начало работы

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&color=F7F7F7&multiline=true&width=750&height=165&lines=%25+git+clone+https%3A%2F%2Fgithub.com%2Fid-andyyy%2FMusical-Studying.git;%25+cd+Musical-Studying;%25+pip+install+-r+requirements.txt;%25+python+manage.py+migrate;%25+python+manage.py+createsuperuser;%25+python+manage.py+runserver)](https://git.io/typing-svg)

```sh
git clone https://github.com/id-andyyy/Musical-Studying.git
cd Musical-Studying
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Обратная связь

Буду признателен, если вы поставите звезду&nbsp;&#11088;. Если вы нашли баг или у вас есть предложения по улучшению,
используйте раздел [Issues](https://github.com/id-andyyy/Musical-Studying/issues).

Read in [English&nbsp;&#127468;&#127463;](README-en.md)

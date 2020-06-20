# Morelia Qt - мессенджер (клиент) для платформы Windows #
-----------------------------------------------------------

## В репозитории 2 бранча: ##

[master](https://github.com/MoreliaTalk/morelia_client_qt/tree/master) - Основная ветка.

[develop](https://github.com/MoreliaTalk/morelia_client_qt/tree/develop) - Ветка для разработчиков.

## В разработке применяется: ##

* [Python 3.8](https://www.python.org/) - язык программирования
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) как основной фронтед фреймворк


## Установка ##

Загрузить и установить последнюю версию [git](https://git-scm.com/downloads).

Если нужен GUI установить [GitHub Desktop](https://desktop.github.com/).

Настроить Git или GitHub Desktop введя свои `username` и `email` от аккаунта созданного на [github](https://www.github.com).

Форкнуть к себе репозиторий Morelia Qt перейдя по ссылке [Fork](https://github.com/MoreliaTalk/morelia_client_qt/fork).

Клонировать репозиторий к себе на локальный компьютер [Clone](https://github.com/MoreliaTalk/morelia_client_qt.git).
```
git clone https://github.com/MoreliaTalk/morelia_client_qt.git
cd morelia_client_qt
```

Добавит свой форк. Заменить `{username}` на свой username созданный в гитхабе.
```
git remote add fork https://github.com/{username}/morelia_client_qt.git
```

Создать виртуальное окружение (предварительно установить pipenv).
```
pipenv shell
```

Установите все необходимые библиотеки
```
pipenv update
```

Если используется pip, то установить библиотеки следующим образом
```
pip install -r requirements.txt
```

Создаем свой бранч со своим именем
```
git branch {имя бранча}
```

### Начинай кодить! ###

Для добавления своего кода в ветку [develop](https://github.com/MoreliaTalk/morelia_client_qt/tree/develop)
```
git pull request origin develop
```

## Требования к стилю кода ##

Перед началом работы рекомендуется прочитать [PEP 8 - руководство по написанию кода на Python](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html). Обязательно использовать линтер (flake8, pylint или подобный).

### дополнительные требования к коду ###
Отсутствуют



---------------------------------------------------------------------------------------------------------------------

## Контакты: ##

[Telegram](https://t.me/joinchat/LImHShzAmIWvpMxDTr5Vxw) - группа где обсуждаются насущные вопросы.

[Trello](https://trello.com/b/qXjJFTP3/develop) - kanban-доска для проекта.

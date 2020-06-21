# Morelia Qt - мессенджер (клиент) для платформы Windows #

## В репозитории 2 бранча ##

[master](https://github.com/MoreliaTalk/morelia_client_qt/tree/master) - Основная ветка.

[develop](https://github.com/MoreliaTalk/morelia_client_qt/tree/develop) - Ветка для разработчиков.

## В разработке применяется ##

* [Python 3.8](https://www.python.org/) - язык программирования
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) как основной фронтед фреймворк

## Установка ##

Загрузить и установить последнюю версию [git](https://git-scm.com/downloads).

Если нужен GUI установить [GitHub Desktop](https://desktop.github.com/).

Настроить Git или GitHub Desktop введя свои `username` и `email` от аккаунта созданного на [github](https://www.github.com).

## Форк репозитория Morelia Qt ##

Форкнуть к себе репозиторий Morelia Qt перейдя по ссылке [Fork](https://github.com/MoreliaTalk/morelia_client_qt/fork).

Клонировать форкнутый репозиторий к себе на локальный компьютер

```cmd
git clone https://github.com/{username}/morelia_client_qt.git
cd morelia_client_qt
```

Переключаемся на ветку develop

```cmd
git checkout develop
```

Синхронизируем свой форк с оригинальным репозиторием `upstream` Morelia Qt

```cmd
git remote add upstream https://github.com/MoreliaTalk/morelia_client_qt.git
```

Проверяем появились ли репозиторий `upstream` в списке удалённых репозиториев

```cmd
git remote -v
> origin    https://github.com/{username}/morelia_client_qt.git (fetch)
> origin    https://github.com/{username}/morelia_client_qt.git (push)
> upstream  https://github.com/MoreliaTalk/morelia_client_qt.git (fetch)
> upstream  https://github.com/MoreliaTalk/morelia_client_qt.git (push)
```

## Создание пулл-реквеста для внесенния изменений в develop-ветку Morelia Qt ##

Получение последних изменнений из develop-ветки Morelia Qt

```cmd
git pull upstream develop
```

Отправка изменений в develop-ветку своего форка

```cmd
git push
```

Для создания пулл-реквеста, необходимо перейти на [GitHub](https://www.github.com), выбрать свой форк и в правом меню нажать на `New pull request`, после чего выбрать бранч из которого будет производится перенос изменений в develop-ветку Morelia Qt и нажать `Create pull request`.

## Настройка виртуального окружения Pipenv ##

Если не установлен pipenv

```cmd
python -m pip install pipenv
```

Создать виртуальное окружение в директории с проектом

```cmd
pipenv shell
```

Установить все требуемые библиотеки из Pipfile

```cmd
pipenv install --ignore-pipfile
```

## Требования к стилю кода ##

Перед началом работы рекомендуется прочитать [PEP 8 - руководство по написанию кода на Python](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html). Обязательно использовать линтер (flake8, pylint или подобный).


## Контакты ##

[Telegram](https://t.me/joinchat/LImHShzAmIWvpMxDTr5Vxw) - группа где обсуждаются насущные вопросы.

[Trello](https://trello.com/b/qXjJFTP3/develop) - kanban-доска для проекта.

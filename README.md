# Table of contents

  - [How to use](#how-to-use)
    - [Pipenv](#pipenv)
  - [Code of conduct](#code-of-conduct)
    - [Conventional commits](#conventional-commits)
      - [Пример](#пример)
      - [Пример интеграции с JIRA](#пример-интеграции-с-jira)
    - [Pull Requests](#pull-requests)

## How to use

### Pipenv

Данный репозиторий использует специальный менеджер пакетов - [Pipfile]((https://pipenv.pypa.io/en/latest/)).

> ;TLDR: в кратце, он удобнее, т.к самостоятельно создает виртуальное окружение и работа с зависимостями там выполнена в более удобном стиле

По данной [ссылке](https://pipenv.pypa.io/en/latest/basics/) можно ознакомиться с базовыми командами

## Code of conduct

### Conventional commits

[Типы коммитов и как их писать](https://platform.uno/docs/articles/uno-development/git-conventional-commits.html)

#### Пример

`feat(users): Implement authorization`

Если используется система для введения задач, то в начале необходимо указать её номер:

#### Пример интеграции с JIRA

`MEGA-123 feat(users): Implement authorization`

### Pull Requests

1. Когда Вы беретесь за задачу, в первую очередь Вы должны создать отдельную ветку с master/main по следующему принципу:

    Задача (MEGA-123): Реализовать JWT авторизацию для всех пользователей

    В таком случае мы создаем новую ветку следующим образом:

    `git checkout -b MEGA-123-jwt-authorization`

    Подробнее о том, как указать задачу [здесь](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/)

2. После того, как Вы закончите работу над задачей, вы должны убедиться, что все проверки пройдены, к примеру все тесты проходят успешно (ни один не зафейлился), все файлы отформатированы по стандартам с помощью дополнительных инструментов (black, flake8, etc.). 

    В данном репозитории присутствует шаблон для pre-commit хуков, которые позволяют сделать эту проверку автоматически перед коммитом. 

    Подробнее про pre-commit hooks - [здесь](https://pre-commit.com/)

3. Затем на платформе по контролю версий после создания PR, необходимо добавить подробное описание о выполненной работе и указать в reviewer'ах другого разработчика. Только после того, как выбранный разработчик одобрит PR и все проверки будут выполнены, можно будет перейти к merge операции.

TBA
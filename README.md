#### Здесь представлено несколько простых автотестов API для сайта https://demowebshop.tricentis.com
<h6>
<ul>
<li>Все тесты реализованы с использованием шаблона <i>PageObject</i></li>
<li>Разработаны на <i>Python</i></li>
<li>Запускаются из <i>Jenkins</i></li>
<li>Для запуска браузера используется <i>Selenoid</i></li>
<li>В результате генерируется отчет при помощи <i>Allure</i> и отправляется нотифкация в <i>Telegram</i></li>
</ul>
</h6>

<h2>Description</h2>
<li><a href="#tools">Инструменты</a></li>
<li><a href="#tests">Тесты</a></li>
<li><a href="#run-tests">Запуск тестов</a></li>
<li><a href="#test-example">Примеры</a></li>

---

<h2 id="tools">Инструменты</h2>
<div align="center">
    <img title="Python" width="40" src="resources/images/python-original.svg">
    <img title="Pytest" width="40" src="resources/images/pytest-original-wordmark.svg">    
    <img title="PyCharm" width="40" src="resources/images/pycharm-original.svg">
    <img title="Selenium" width="40" src="resources/images/selenium.png">
    <img title="Selene" width="40" src="resources/images/selene.png">
    <img title="Jenkins" width="40" height="40" src="resources/images/jenkins-original.svg">
    <img title="Selenoid" width="40" src="resources/images/selenoid.png">
    <img title="Allure" width="40" src="resources/images/allure.png">
    <img title="AllureTestOps" width="40" src="resources/images/allure_testops.svg">
    <img title="Github" width="40" src="resources/images/github-original-wordmark.svg">
    <img title="Telegram" width="40" src="resources/images/telegram.png">
</div>

---

<h2 id="tests">Автоматизированные тесты</h2>
<ul>
<li>Попытка регистрации с неправильным email</li>
<li>Попытка входа без логина и пароля</li>
<li>Поиск по базе знаний</li>
<li>Фильтрация в разделе Аналитика</li>
<li>Попытка добавления канала без ссылки</li>
<li>Проверка, что вразделе FAQ отображается нужный текст</li>
<li>Проверка загрузки горячих предложений</li>    
</ul>

---

<h2 id="tests">Ручные тесты</h2>
<ul>
<li>Переключение чекбокса с "Заказчикам" на "Владельцу канала"</li>
<li>Переключение чекбокса с "Владельцу канала" на "Заказчикам"</li>    
</ul>

---

<h2 id="run-tests">Запуск тестов</h2>

<pre>
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest ${TESTS_FOLDER} || true
</pre>

---

<h2 id="test-example">Примеры запуска</h2>

<h3>Jenkins</h3>

https://jenkins.autotests.cloud/job/C012-MiledyDarkness_qa_guru_22_telega_ui/
<img src="resources/images/job_in_jenkins.jpg" height="300">

#### История запусков тестового набора
https://jenkins.autotests.cloud/job/C012-MiledyDarkness_qa_guru_22_telega_ui/allure/
<img src="resources/images/history_of_runs.jpg" height="300">

#### Пример выполнения одного теста
<img src="resources/images/example_of_run.jpg" height="300">

---
<h3>Allure TestOps</h3>

https://allure.autotests.cloud/project/4277/dashboards

<img src="resources/images/allure_testops_job.jpg" height="300">

#### Совместное хранение ручных и автоматизированных тест-кейсов
<img src="resources/images/allure_testops_cases.jpg" height="300">

---

#### Сообщение в телеграмм 
<img src="resources/images/tg_notifications.jpg" height="300">

#### Видео
![](resources/images/test_analytics_filter.gif)
---

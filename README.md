# Проект по автоматизации тестирования для компании [MWI](https://mwi.me/)
> MWI — полносервисное digital-агентство с собственным отделом разработки
## **Содержание:**
____
* <a href="#tools">Технологии и инструменты</a>
* <a href="#cases">Примеры автоматизированных тест-кейсов</a>
* <a href="#jenkins">Сборка в Jenkins</a>
* <a href="#console">Запуск из терминала</a>
* <a href="#allure">Allure отчет</a>
* <a href="#allure-testops">Интеграция с Allure TestOps</a>
* <a href="#jira">Интеграция с Jira</a>
* <a href="#telegram">Уведомление в Telegram при помощи бота</a>
* <a href="#video">Примеры видео выполнения тестов на Selenoid</a>
----
<a id="tools"></a>
## <a name="Технологии и инструменты">**Технологии и инструменты:**</a>

<p align="center">  
<a href="https://www.jetbrains.com/idea/"><img src="images/logo/pycharm-original.svg" width="50" height="50"  alt="PyCharm"/></a>  
<a href="https://www.java.com/"><img src="images/logo/python-original.svg" width="50" height="50"  alt="Python"/></a>  
<a href="https://github.com/"><img src="images/logo/github-original.svg" width="50" height="50"  alt="Github"/></a>
<a href="https://aerokube.com/selenoid/"><img src="images/logo/selenium-svgrepo-com.svg" width="50" height="50"  alt="Selenoid"/></a>  
<a href="ht[images](images)tps://github.com/allure-framework/allure2"><img src="images/logo/Allure.png" width="50" height="50"  alt="Allure"/></a> 
<a href="https://qameta.io/"><img src="images/logo/AllureTestOps.png" width="50" height="50"  alt="Allure TestOps"/></a>   
<a href="https://www.jenkins.io/"><img src="images/logo/jenkins-original.svg" width="50" height="50"  alt="Jenkins"/></a>  
<a href="https://www.atlassian.com/ru/software/jira/"><img src="images/logo/jira-original-wordmark.svg" width="50" height="50"  alt="Jira"/></a>  
</p>

<a id="cases"></a>
## <a name="Примеры автоматизированных тест-кейсов">**Примеры автоматизированных тест-кейсов:**</a>
____
-  *Проверка успешной отправки заявки через попап*
-  *Клик по пункту меню "Портфолио" открывает страницу с проектами*
-  *Проверка отображения, кликабельности кнопки "Скачать презентацию*
-  *Проверка возможности отправки заявки с некорректным номером телефона*
-  *Отправка заявки c пустым значением поля "ИМЯ"'*


____
<a id="jenkins"></a>
## <img alt="Jenkins" height="25" src="images/logo/jenkins-original.svg" width="25"/></a><a name="Сборка"></a>Сборка в [Jenkins](https://jenkins.autotests.cloud/job/Kod3ik_qa_guru_x5/)</a>
____
<p align="center">  
<a href="https://jenkins.autotests.cloud/job/Kod3ik_qa_guru_x5/"><img src="images/screen/JenkinsScreen.png" alt="Jenkins" width="950"/></a>  
</p>


### **Параметры сборки в Jenkins:**

- *browser (браузер, по умолчанию chrome)*
- *browserVersion (версия браузера, по умолчанию 128.0)*
- *browserSize (размер окна браузера, по умолчанию 1920x1080)*
- *baseUrl (адрес тестируемого веб-сайта)*
- *remoteUrl (логин, пароль и адрес удаленного сервера Selenoid)*

<a id="console"></a>
## Команды для запуска из терминала
___
***Локальный запуск:***
```bash  
pytest tests/
```

***Удалённый запуск через Jenkins:***
```bash  
pytest tests/ \
  --browser=${browser} \
  --browser-version=${browserVersion} \
  --browser-size=${browserSize} \
  --base-url=${baseUrl} \
  --remote-url=${remoteUrl}
```
___
<a id="allure"></a>
## <img alt="Allure" height="25" src="images/logo/Allure.png" width="25"/></a> <a name="Allure"></a>Allure [отчет](https://jenkins.autotests.cloud/view/python_students/job/python_test_ismailov_hw14/16/allure/)</a>
___

### *Основная страница отчёта*

<p align="center">  
<img title="Allure Overview Dashboard" src="images/screen/AllureResultMain.png" width="850">  
</p>

___
### *Тест-кейсы*

<p align="center">  
<img title="Allure Tests" src="images/screen/AllureTestCases.png" width="850">  
</p>

___
### *Графики*
  <p align="center">  
<img title="Allure Graphics" src="images/screen/AllureGraphs.png" width="850">

___
<a id="allure-testops"></a>
## <img alt="Allure" height="25" src="images/logo/AllureTestOps.png" width="25"/></a>Интеграция с <a target="_blank" href="https://allure.autotests.cloud/project/5153/dashboards">Allure TestOps</a>
____
### *Allure TestOps Dashboard*

<p align="center">  
<img title="Allure TestOps Dashboard" src="images/screen/TestOppsDashboard.png" width="850">  
</p>  

### *Авто тест-кейсы*

<p align="center">  
<img title="Allure TestOps Tests" src="images/screen/TestOppsTestCases.png" width="850">  
</p>

___
<a id="jira"></a>
## <img alt="Allure" height="25" src="images/logo/jira-original-wordmark.svg" width="25"/></a> Интеграция с <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1591">Jira</a>
____
<p align="center">  
<img title="Jira" src="images/screen/JiraScreen.png" width="850">  
</p>

____
<a id="telegram"></a>
## <img alt="Allure" height="25" src="images/logo/telegram-svgrepo-com.svg" width="25"/></a> Уведомление в Telegram
____
<p align="center">  
<img title="Allure Overview Dashboard" src="images/screen/telegram_notification.png" width="550">  
</p>





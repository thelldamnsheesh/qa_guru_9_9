import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open("https://github.com")

@allure.step('Ищем нужный репозиторий')
def searching_for_repository():
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

@allure.step('Переходим в репо')
def open_repository():
    s(by.link_text("eroshenkoam/allure-example")).click()

@allure.step('Переходим во вкладку Issues')
def open_issue():
    s("#issues-tab").click()

@allure.step('Проверяем наличие Issue с номером 76')
def check_issue():
    s(by.partial_text("#76")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "zeleninevgeny")
@allure.feature("Задачи в репозитории")
@allure.story(" Есть нужная issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_selene_main():
    open_main_page()
    searching_for_repository()
    open_repository()
    open_issue()
    check_issue()
import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com")

    with allure.step('Ищем нужный репозиторий'):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step('Переходим в репо'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Переходим во вкладку Issues'):
        s("#issues-tab").click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text("#76")).should(be.visible)
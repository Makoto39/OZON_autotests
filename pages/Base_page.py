from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # найти элемент и кликнуть по нему
    def find_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()

    # Проверить видимость элемента
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # # Проверить видимость элемента
    # def move_to_element(self, by_locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).move_to_element()

    # Ввод данных в строку ввода
    def input_keys(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Получить заголовок окна
    def get_windows_title(self, text) -> bool:
        element = windows_title = WebDriverWait(self.driver, 5).until(EC.title_contains(text))
        return bool(element)

    # Получить атрибут текст элемента
    def get_text_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Найти элемент
    def find_one_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    # Отобразить суб-меню , перейти в нем к кнопке = только вход на главную страницу
    def click_catalog_move_to_submenu(self, by_locator, submenu_locator):
        main_menu = self.find_one_element(by_locator)
        submenu = self.find_one_element(submenu_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu)
        action.click(main_menu).perform()
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submenu))
        action.click(submenu).perform()

    # Очистить поле ввода, ввод текста и нажать Enter
    def clear_field_and_send_text_with_enter(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(5)
        # action.perform()
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(u'\ue007')
        # input_field.send_keys(Keys.ENTER)

    # Очистить поле ввода, ввод текста
    def clear_field_and_send_text(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(5)
        # action.perform()
        input_field.clear()
        input_field.send_keys(text)

    # Дождаться полного списка элементов
    def find_all_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    # Отобразить popup окно
    def show_popup_window(self, by_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()

    # Убрать курсор с элемента
    def put_away_from_element(self, by_locator):
        element_to_move = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(element_to_move).perform()

    # Проверить невидимость элемента
    def isnt_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

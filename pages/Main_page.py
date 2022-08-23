from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os,pickle

from pages.Base_page import BasePage
from config import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    MAIN_LOGO = (By.CSS_SELECTOR, "#stickyHeader div")
    CATALOG = (By.CSS_SELECTOR, "div[data-widget ='catalogMenu'] div button")
    ELECTRONICA_SUB = (By.XPATH, "//a[@class = 'a3p5 g5s4 g5s6 g5t' and @href='/category/elektronika-15500/']")
    #ELECTRONICA = (By.XPATH, "//span[@class ='g5s7' and contains (text(), 'Электроника')]")
    #ELECTRONICA = (By.XPATH, "//a[@class = 'a3p5 g5e3' and @href='/category/elektronika-15500/']")
    HEAD_OF_PAGE_ELECTRONICA_SUB = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    SEARCH_WHERE = (By.CSS_SELECTOR, "div[data-widget = 'searchBarDesktop'] form div span")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder = 'Искать на Ozon']")
    SUBMIT_SEARCH = (By.XPATH, "//button[@class = 'f9k']")
    ENTRANCE = (By.CSS_SELECTOR, "div[data-widget = 'profileMenuAnonymous']")
    POPUP_WINDOW_ENTRANCE = (By.XPATH, "//div[@class = 'ui-i8']")
    FAVORITES = (By.XPATH, "//a[@href = '/my/favorites']")
    HEAD_OF_PAGE_FAVORITES = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Избранное')]")
    CART = (By.XPATH, "//a[@href = '/cart']")
    ORDERS = (By.CSS_SELECTOR, "div[data-widget = 'orderInfo']")
    TOPFASHION = (By.XPATH, "//a[@href = '/highlight/top-fashion/' and @class = 'a3p5 g5e3']")
    HEAD_OF_PAGE_TOP_FASHION = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'TOP Fashion')]")
    Premium = (By.XPATH, "//a[@href = '/highlight/premium/' and @class = 'a3p5 g5e3']")
    OZON_TRAVEL = (By.XPATH, "//a[@href = 'https://www.ozon.ru/travel?perehod=ozon_menu_header' and @class = 'a3p5 g5e3']")
    SEARCH_SUBMIT = (By.CSS_SELECTOR, "#stickyHeader > div.cr4 > div > form > button > svg")
    OZON_BANK = (By.XPATH, "//a[@href = 'https://bank.ozon.ru/bank' and @class = 'a3p5 g5e3']")
    LIVE = (By.XPATH, "//a[@href = '/live/' and @class = 'a3p5 g5e3']")
    ACTIONS = (By.XPATH, "//a[@href = '/info/actions/' and @class = 'a3p5 g5e3']")
    HEAD_OF_PAGE_ACTIONS = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Акции и спецпредложения')]")
    BRENDS = (By.XPATH, "//a[@href = '/brand/' and @class = 'a3p5 g5e3']")
    HEAD_OF_PAGE_BRENDS = (By.XPATH, "//h1[@class = 'a9u6 f-h1' and contains (text(), 'Все бренды')]")
    HEAD_OF_WINDOW_SELECT_CITY = (By.XPATH, "//h1[@class = 'a9u6 f-h1' and contains (text(), 'Все бренды')]")
    SHOPS = (By.XPATH, "//a[@href = '/seller/' and @class = 'a3p5 g5e3']")
    HEAD_OF_PAGE_SHOPS = (By.XPATH, "//div[@class = 'g2f8' and contains (text(), 'Все магазины')]")
    ELECTRONICA_MAIN = (By.XPATH, "//a[@href = '/category/elektronika-15500/' and contains (text(), 'Электроника')]")
    HEAD_OF_PAGE_ELECTRONICA_MAIN = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    CLOTHES_AND_SHOES = (By.XPATH, "//a[@href = '/info/main-apparel/' and contains (text(), 'Одежда и обувь')]")
    CHAPTER_OF_CLOTHES_AND_SHOES = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Женщинам')]")
    KIDS_GOODS = (By.XPATH, "//a[@href = '/category/detskie-tovary-7000/' and contains (text(), 'Детские товары')]")
    HEAD_OF_PAGE_KIDS_GOODS = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Детские товары')]")
    HOUSE_AND_GARDEN = (By.XPATH, "//a[@href = '/category/dom-i-sad-14500/' and contains (text(), 'Дом и сад')]")
    HEAD_OF_PAGE_HOUSE_AND_GARDEN = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Дом и сад')]")
    BUTTON_SELECT_CITY = (By.XPATH, "//button[@type = 'button' and @class = 'ui-b2']")
    INPUT_FIELD_CITY = (By.XPATH, "//input[@class = 'ui-g ui-g2' and @type = 'text']")
    LIST_OF_SUITABLE_CITIES = (By.XPATH, "//ul[@class = 'a3i7']")










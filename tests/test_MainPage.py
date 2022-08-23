from pages.Main_page import MainPage
from config import TestData


# Логотип Ozon (переход в раздел нг подарки) виден на странице
def test_main_logo_on_page(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.MAIN_LOGO)
    assert logo == True


# Попадаем в раздел Global Promo при клике по лого Ozon
def test_logo_ozon_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIN_LOGO)
    title_of_window = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_MAIN_LOGO)
    assert title_of_window == True


# Кнопка "Каталог" видна на странице
def test_button_catalog_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CATALOG)
    assert button == True


# Кнопка "Каталог" имеет верное название
def test_button_catalog_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.CATALOG)
    assert button_name == TestData.NAME_OF_BUTTON_CATALOG


# Кнопка локализации поиска видна на странице
def test_search_where_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.SEARCH_WHERE)
    assert button == True


# Строка поиска видна на странице
def test_search_on_page(driver):
    main_page = MainPage(driver)
    field_input = main_page.is_visible(MainPage.SEARCH_INPUT)
    assert field_input == True


# Кнопка подтверждения ввода в строку поиска видна на странице
def test_submit_search_on_page(driver):
    main_page = MainPage(driver)
    submit_search = main_page.is_visible(MainPage.SEARCH_SUBMIT)
    assert submit_search == True


#
# Кнопка Войти видна на странице
def test_entrance_on_page(driver):
    main_page = MainPage(driver)
    entrance = main_page.is_visible(MainPage.ENTRANCE)
    assert entrance == True


# При наведении на кнопку Войти появляется всплывающее окно
def test_popup_window_appear(driver):
    main_page = MainPage(driver)
    main_page.show_popup_window(MainPage.ENTRANCE)
    popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window == True


# Всплывающее окно исчезает, когда курсор уводим с кнопки Войти
def test_popup_window_message_button_disappeared(driver):
    main_page = MainPage(driver)
    main_page.show_popup_window(MainPage.ENTRANCE)
    popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window == True
    main_page.put_away_from_element(MainPage.FAVORITES)
    popup_window_disappeared = main_page.isnt_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window_disappeared is True


# Кнопка Заказы видна на странице
def test_button_Orders_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ORDERS)
    assert button == True


# Кнопка Избранное видна на странице
def test_button_favorites_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.FAVORITES)
    assert button == True


#
# Кнопка Избранное кликабельна, попадаем в соответствующий раздел
def test_favorites_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FAVORITES)
    Favorites_page_header = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_FAVORITES)
    assert Favorites_page_header == TestData.HEADER_OF_PAGE_FAVORITES


# Кнопка Корзина видна на странице
def test_button_cart_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CART)
    assert button == True


# Кнопка Корзина кликабельна и попадаем в соответствующий раздел
def test_cart_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CART)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_CART)
    assert window_title == True


# Кнопка раздела TopFashion видна на странице
def test_button_top_fashion_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.TOPFASHION)
    assert button == True


# Кнопка TOPFashion имеет верное название
def test_button_top_fashion_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.TOPFASHION)
    assert button_name == TestData.NAME_OF_BUTTON_TOP_FASHION


#
# Кнопка TopFashion кликабельна и попадаем в соответствующий раздел
def test_topFashion_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.TOPFASHION)
    page_header = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_TOP_FASHION)
    assert page_header == TestData.TOP_FASHION


# Кнопка раздела Premium видна на странице
def test_button_Premium_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.Premium)
    assert button == True


# Кнопка "Premium" имеет верное название
def test_button_premium_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.Premium)
    assert button_name == TestData.NAME_OF_BUTTON_Premium


# #Кнопка раздела Ozon travel видна на странице
def test_button_ozon_travel_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_TRAVEL)
    assert button == True


# Кнопка Ozon travel имеет верное название
def test_button_ozon_travel_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_TRAVEL)
    assert button_name == TestData.NAME_OF_BUTTON_OZON_TRAVEL


# Кнопка Ozon travel кликабельна, попадаем в соответствующий раздел
def test_Ozon_travel_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_TRAVEL)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_OZON_TRAVEL)
    assert window_title == True


# Кнопка раздела Ozon счет видна на странице
def test_button_Ozon_bank_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_BANK)
    assert button == True


# Кнопка Ozon счет имеет верное название
def test_button_ozon_bank_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_BANK)
    assert button_name == TestData.NAME_OF_BUTTON_OZON_BANK


# Кнопка Ozon счет кликабельна, попадаем в соответствующий раздел
def test_Ozon_bank_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_BANK)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_OZON_BANK)
    assert window_title == True


# Кнопка раздела LIVE счет видна на странице
def test_button_LIVE_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.LIVE)
    assert button == True


# Кнопка LIVE имеет верное название
def test_button_LIVE_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.LIVE)
    assert button_name == TestData.NAME_OF_BUTTON_LIVE


# Кнопка Ozon LIVE кликабельна, попадаем в соответствующий раздел
def test_LIVE_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.LIVE)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_LIVE)
    assert window_title == True


# Кнопка раздела Акции счет видна на странице
def test_button_actions_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ACTIONS)
    assert button == True


# Кнопка Акции имеет верное название
def test_button_action_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ACTIONS)
    assert button_name == TestData.NAME_OF_BUTTON_ACTIONS


# Кнопка Акции кликабельна, попадаем в соответствующий раздел
def test_actions_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ACTIONS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_ACTIONS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_ACTIONS


#  #Кнопка раздела Бренды видна на странице
def test_button_brands_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.BRENDS)
    assert button == True


# Кнопка Бренды имеет верное название
def test_button_brands_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.BRENDS)
    assert button_name == TestData.NAME_OF_BUTTON_BRANDS


#
# Кнопка Бренды кликабельна, попадаем в соответствующий раздел
def test_brends_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BRENDS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_BRENDS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_BRENDS


#  #Кнопка раздела Магазины видна на странице
def test_button_shops_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.SHOPS)
    assert button == True


# Кнопка Магазины кликабельна, попадаем в соответствующий раздел
def test_shops_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.SHOPS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_SHOPS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_SHOPS


#  #Кнопка раздела Электроника видна на странице
def test_button_electronica_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ELECTRONICA_MAIN)
    assert button == True


# Кнопка раздела Электроника имеет верное название
def test_button_electronics_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ELECTRONICA_MAIN)
    assert button_name == TestData.NAME_OF_BUTTON_ELECTRONICA_MAIN


# Кнопка Электроника кликабельна, попадаем в соответствующий раздел
def test_electronica_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ELECTRONICA_MAIN)
    window_title = main_page.get_text_of_element(MainPage.ELECTRONICA_MAIN)
    assert window_title == TestData.HEADER_OF_PAGE_OF_ELECTRONICA_MAIN


# Кнопка раздела Одежда и обувь видна на странице
def test_button_clothes_and_shoes_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CLOTHES_AND_SHOES)
    assert button == True


# #Кнопка раздела Одежда и обувь имеет верное название
def test_button_clothes_and_shoes_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.CLOTHES_AND_SHOES)
    assert button_name == TestData.NAME_OF_BUTTON_CLOTHES_AND_SHOES


# Кнопка Одежда и обувь кликабельна, попадаем в соответствующий раздел
# Присутствует раздел "Женщинам"
def test_clothes_and_shoes_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CLOTHES_AND_SHOES)
    window_title = main_page.get_text_of_element(MainPage.CHAPTER_OF_CLOTHES_AND_SHOES)
    assert window_title == TestData.HEADER_OF_CHAPTER_OF_CLOTHES_AND_SHOES


# Кнопка раздела Детские товары видна на странице
def test_button_kids_goods_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.KIDS_GOODS)
    assert button == True


# #Кнопка раздела Детские товары имеет верное название
def test_button_kids_goods_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.KIDS_GOODS)
    assert button_name == TestData.NAME_OF_BUTTON_KIDS_GOODS


# Кнопка Детские товары кликабельна, попадаем в соответствующий раздел
def test_kids_goods_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.KIDS_GOODS)
    window_title = main_page.get_text_of_element(MainPage.KIDS_GOODS)
    assert window_title == TestData.HEADER_OF_PAGE_OF_KIDS_GOODS


# Кнопка раздела Дом и сад видна на странице
def test_button_house_and_garden_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.HOUSE_AND_GARDEN)
    assert button == True


# #Кнопка раздела Дом и сад имеет верное название
def test_button_house_and_garden_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.HOUSE_AND_GARDEN)
    assert button_name == TestData.NAME_OF_BUTTON_HOUSE_AND_GARDEN


# Кнопка Дом и сад кликабельна, попадаем в соответствующий раздел
def test_button_house_and_garden_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.HOUSE_AND_GARDEN)
    window_title = main_page.get_text_of_element(MainPage.HOUSE_AND_GARDEN)
    assert window_title == TestData.HEADER_OF_PAGE_OF_HOUSE_AND_GARDEN


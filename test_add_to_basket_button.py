link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    is_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    try:
        assert is_button #сравнение с 0 не нужно, ассерт падает если массив пустой
    except:
        raise pytest.NoSuchElementError("basket button is not exist")

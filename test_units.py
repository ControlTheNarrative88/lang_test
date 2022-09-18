import pytest
from selenium.webdriver.common.by import By


def test_add_to_chart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")


if __name__ == "__main__":
    pytest.main()

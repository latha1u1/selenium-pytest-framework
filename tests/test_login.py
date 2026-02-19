from pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")

    message = login_page.get_message()

    assert "You logged into a secure area!" in message

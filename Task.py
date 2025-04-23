#
# from selenium.webdriver.common.by import By
# from RPA.Browser.Selenium import Selenium
# import time
# from RPA.Robocorp.WorkItems import WorkItems
#
# class LA_Times:
#     def __init__(self):
#         self.browser= Selenium()
#         self.browser.open_available_browser("https://www.latimes.com/",maximized=True)
#
#
#     def search_bar(self):
#
#         self.browser.click_element_when_visible("//button[@class='flex justify-center items-center h-10 py-0 px-2.5 bg-transparent border-0 text-header-text-color cursor-pointer transition-colors hover:opacity-80 xs-5:px-5 md:w-10 md:p-0 md:ml-2.5 md:border md:border-solid md:border-header-border-color md:rounded-sm lg:ml-3.75']")
#         self.browser.input_text("//input[@placeholder='Search']","Pakistan")
#         self.browser.click_element_when_visible("//input[@placeholder='Search']")
#         time.sleep(15)
#
#
#
#
# p=LA_Times()
# p.search_bar()


# import os
# import time
# import logging
# from RPA.Browser.Selenium import Selenium
# from datetime import datetime
# from RPA.Robocorp.WorkItems import WorkItems
#
# # Set up logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
# logger = logging.getLogger(__name__)
#
# class W3SchoolsRPA:
#     def __init__(self, email: str, password: str):
#         """Initialize the W3SchoolsRPA class with email and password."""
#         self.email = email
#         self.password = password
#         self.browser = Selenium()
#
#
#     def open_website(self):
#
#         self.browser.open_available_browser("https://www.w3schools.com/")
#         self.browser.maximize_browser_window()
#
#     def click_login_button(self):
#         """Click the login button."""
#         login_button_xpath = "//a[@class='user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login']"
#         self.browser.click_element_when_visible(login_button_xpath)
#         logger.info("Clicked login button")
#
#
#
#     def enter_email(self):
#         """Enter email into the Google login page."""
#         email_field_xpath = "// input[ @ placeholder = 'email']"
#         self.browser.input_text(email_field_xpath, self.email)
#         self.browser.press_keys(email_field_xpath, "ENTER")
#         time.sleep(2)  # Wait for the next page to load
#
#     def enter_password(self):
#         """Enter password into the Google login page."""
#         password_field_xpath = "// input[ @ placeholder = 'password']"
#         self.browser.input_text(password_field_xpath, self.password)
#         self.browser.press_keys(password_field_xpath, "ENTER")
#         time.sleep(5)  # Wait for the login to complete
#
#     def click_continue(self):
#         """Click the 'Continue' button after login."""
#         continue_button_xpath = "//button[normalize-space()='Login']"
#         self.browser.click_element_when_visible(continue_button_xpath)
#         logger.info("Clicked 'Continue' button")
#
#
#
#
#
#     def run(self):
#         """Run the entire RPA process."""
#         try:
#             self.open_website()
#             self.click_login_button()
#
#             self.enter_email()
#             self.enter_password()
#             self.click_continue()
#
#         except Exception as e:
#             logger.error(f"An error occurred: {e}")
#
#
# if __name__ == "__main__":
#     # Replace with your actual email and password
#     email = "chaudharyabubakar702@gmail.com"
#     password = "12526252aA!"
#
#     # Initialize the RPA class and run the automation
#     w3schools_rpa = W3SchoolsRPA(email, password)
#     w3schools_rpa.run()



import os
import time
import logging
from RPA.Browser.Selenium import Selenium
from typing import Any
from selenium.common.exceptions import NoSuchWindowException, InvalidSessionIdException, WebDriverException

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def handle_error_and_retry(func: callable) -> callable:
    def wrapper(self: Any, *args, **kwargs) -> callable:
        retry_count = 2
        while retry_count > 0:
            try:
                return func(self, *args, **kwargs)
            except Exception as exception:
                logger.error(f"An error occurred during {func.__name__}: {str(exception)}")
                retry_count -= 1
                if retry_count == 0:
                    raise exception

                logger.info(f"Retrying... {retry_count} attempts left.Closing ")
                self.close_browser_and_reopen()
                self.perform_login()
        return None

    return wrapper


class W3SchoolsRPA:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.browser = Selenium()
        self.browser_open = False

    def open_website(self):
        if not self.browser_open:
            self.browser.open_available_browser("https://www.w3schools.com/")
            self.browser.maximize_browser_window()
            self.browser_open = True
            logger.info("Opened the ")
        else:
            logger.info("Browser open.")

    def close_browser_and_reopen(self):
        if self.browser_open:
            logger.info("Closing the browser")
            self.browser.close_browser()
            self.browser_open = False
        time.sleep(2)
        self.open_website()

    def click_login_button(self):
        login_button_xpath = "//a[@class='user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login']"
        self.browser.click_element_when_visible(login_button_xpath)
        logger.info("Clicked login button")

    def enter_email(self):
        email_field_xpath = "//input[@placeholder='email']"
        self.browser.input_text(email_field_xpath, self.email)
        self.browser.press_keys(email_field_xpath, "ENTER")
        time.sleep(2)

    def enter_password(self):
        password_field_xpath = "//input[@placeholder='password']"
        self.browser.input_text(password_field_xpath, self.password)
        self.browser.press_keys(password_field_xpath, "ENTER")
        time.sleep(5)

    @handle_error_and_retry
    def perform_login(self):

        self.open_website()
        self.click_login_button()
        self.enter_email()
        self.enter_password()

    def run(self):
        try:
            logger.info("Starting first ")
            self.perform_login()

            logger.info("Now performing second ")
            self.close_browser_and_reopen()
            self.perform_login()

        except Exception as e:
            logger.error(f"Login failed after retry: {e}")
            raise


if __name__ == "__main__":
    email = "chaudharyabubakar702@gmail.com"
    password = "12526252aA!"
    w3schools_rpa = W3SchoolsRPA(email, password)
    w3schools_rpa.run()
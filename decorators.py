# # def capture_screenshot_if_error(func: callable) -> callable:
# #     """Decorator to capture screenshot if error occurs."""
# # self.output_dir = os.path.join(os.getcwd(), "output")
# #         if not os.path.exists(self.output_dir):
# #             os.makedirs(self.output_dir)
# #     def wrapper(self: Any, *args, **kwargs) -> callable:
# #         try:
# #             return func(self, *args, **kwargs)
# #         except Exception as exception:
# #             ts = datetime.now().strftime("%H_%M_%S")
# #             file_name = f"{self.__class__.__name__}_{func.__name__}_{ts}.png"
# #             file_path = os.path.join(CONFIG.DIRECTORIES.OUTPUT, file_name)
# #             try:
# #                 self.browser.capture_page_screenshot(file_path)
# #                 logger.info(f"Screenshot saved to {file_path}")
# #                 attach_file_to_exception(exception, file_path)
# #             except (NoSuchWindowException, InvalidSessionIdException) as ex:
# #                 logger.warning(f"Failed to capture screenshot due to error : {str(ex)}")
# #             raise exception
# #
# #
# #
# #     return wrapper
#
#
# from typing import Any
# import logging
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
# logger = logging.getLogger(__name__)
#
#
#
# def back_to_login(func: callable) -> callable:
#     def wrapper(self : Any,*args: Any, **kwargs: Any) -> Any:
#         try:
#             return func(self : A ,*args, **kwargs)
#         except Exception as exception:
#             logger.error(f"An error occurred during {func.__name__}: {str(exception)}")
#             self.return_to_login()
#
#             try:
#                 logging.info(f"Retrying ")
#                 return func(*args, **kwargs)
#             except Exception as retry_exception:
#                 logger.error(f"An error occurred during {func.__name__}: {str(retry_exception)}")
#                 return retry_exception
#
#     return wrapper
#


# import os
# import time
# import logging
# from RPA.Browser.Selenium import Selenium
# from datetime import datetime
# from typing import Any
# from selenium.common.exceptions import NoSuchWindowException, InvalidSessionIdException, WebDriverException
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
# logger = logging.getLogger(__name__)
#
# def handle_error_and_retry(func: callable) -> callable:
#     def wrapper(self: Any, *args, **kwargs) -> callable:
#         retry_count = 3
#         while retry_count > 0:
#             try:
#                 return func(self, *args, **kwargs)
#             except (NoSuchWindowException, InvalidSessionIdException, WebDriverException) as exception:
#                 logger.error(f"An error occurred during {func.__name__}: {str(exception)}")
#                 retry_count -= 1
#                 logger.info(f"Retrying... {retry_count} attempts left.")
#                 if retry_count == 0:
#                     logger.error("Maximum retry attempts reached. Failing.")
#                     raise
#                 self.browser.close_browser()  # Close the browser if it was left in a bad state
#                 self.perform_login()  # Retry the login after an error
#                 time.sleep(2)  # Optionally add a small delay between retries
#             except Exception as exception:
#                 logger.error(f"An unexpected error occurred during {func.__name__}: {str(exception)}")
#                 raise
#     return wrapper








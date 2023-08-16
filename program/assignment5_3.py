from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time

class GitHubLoginAutomation:

    def __init__(self):

        self.driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed and in PATH

    def login(self, username, password):

        self.driver.get("https://github.com/login")

        # Locate username and password fields, and the Sign in button

        username_field = self.driver.find_element(By.NAME, "login")

        password_field = self.driver.find_element(By.NAME, "password")

        sign_in_button = self.driver.find_element(By.NAME, "commit")


        # Input credentials and click the Sign in button

        username_field.send_keys(username)

        password_field.send_keys(password)

        sign_in_button.click()


        # Add a short delay to allow for page to load and potential error message

        time.sleep(2)

        # Check for error message

        error_message = self.driver.find_element(By.CSS_SELECTOR, ".flash-error")

        if error_message.is_displayed():

            return error_message.text

        else:

            return "Login successful"


    def close(self):

        self.driver.quit()


if __name__ == "__main__":

    # Replace these with your test credentials

    test_username = "YOUR MAIL@MAIL.COM"

    test_password = "YOUR PASSWORD"


    # Create an instance of GitHubLoginAutomation

    automation = GitHubLoginAutomation()

    # Attempt to sign in with valid credentials

    result = automation.login(test_username, test_password)

    print("Login result:", result)


    # Attempt to sign in with invalid credentials

    result = automation.login(test_username, "invalid_password")

    print("Login result:", result)


    # Close the automation instance

    automation.close()


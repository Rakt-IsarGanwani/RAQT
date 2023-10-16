import random
import string
from playwright.sync_api import Page

class SignupPage:

    def __init__(self, page:Page):
        self.page = page

        self.Get_started=page.get_by_role('link', name="Get Started")
        self.Name_input=page.get_by_placeholder("Enter your name")
        self.Email_input=page.get_by_placeholder("Enter your email")
        self.Company_input=page.get_by_placeholder("Company")
        self.Password_input=page.get_by_placeholder("Add a password")
        self.Confirm_password_input=page.get_by_placeholder("Confirm password")
        self.Term_check_box=page.locator("//input[@id='sign-up-agree']")
        self.Submit_button=page.locator("//button[normalize-space()='Submit']")
        self.Logo=page.locator("//img[@alt='logo-large']")

    def generate_random_email(self):
        num = random.randint(1, 1000)  
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"isar{num}+{random_chars}@rakt.org"

        
    


    
from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page:Page):
        self.page = page
        
        self.Sign_in=page.get_by_role("navigation").get_by_role("link", name="Sign In")
        self.Email_input=page.get_by_label("Email")
        self.Password_input=page.get_by_label("Password*")
        self.Signin_button=page.locator("//button[normalize-space()='Sign In']")
        self.Connect_button=page.locator("//a[@id='add-sales-channel-button']//img")
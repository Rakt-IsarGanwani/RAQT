#The test_signup has 2 test cases, in the first test case the user signup and we verify that it signup successfully
#In the secound one an already exisitng user tries to sign up and we validate it through the validation message. 

from models.Signup_page import SignupPage
from Utility.Navigation_Links import Page_links
from Utility.Tracing import Tracing_the_test
from playwright.sync_api import Page, expect

#First test case in which new user signs up
def test_New_User_Sign_up(page: Page): 
    At_SignupPage= SignupPage(page)
    HomePage=Page_links(page)
    TestTracing= Tracing_the_test(page.context)
    TestTracing.Start_Trace_test()
    HomePage.navigate()
    At_SignupPage.Get_started.click()
    
    
    At_SignupPage.Name_input.type("Isar1", delay=200)
    At_SignupPage.Name_input.input_value()

    random_email = At_SignupPage.generate_random_email()
    At_SignupPage.Email_input.type(random_email, delay=200)

    At_SignupPage.Company_input.type("Isar_company", delay=200)

    At_SignupPage.Password_input.type("Test@123",delay=200)

    At_SignupPage.Confirm_password_input.type("Test@123", delay=200)

    At_SignupPage.Term_check_box.set_checked(True)

    # At_SignupPage.Submit_button.screenshot(path="startbutton.png")
    At_SignupPage.Submit_button.hover()
    At_SignupPage.Submit_button.click(button="left")
    page.screenshot(path="screenshot.png", full_page=True)
    
    At_SignupPage.Logo.wait_for_selector(timeout=60000)
    
    expect(At_SignupPage.Logo).to_be_visible()
    


#Secound test case in the an existign user tries to sign up
    
def test_Old_User_Sign_up(page: Page): 
    
    At_SignupPage= SignupPage(page)
    HomePage=Page_links(page)
    TestTracing= Tracing_the_test(page.context)
    TestTracing.Start_Trace_test()
    HomePage.navigate()
    At_SignupPage.Get_started.click()
    
    
    At_SignupPage.Name_input.type("Isar1", delay=200)
    At_SignupPage.Name_input.input_value()

    At_SignupPage.Email_input.type("isar+1@rakt.org")

    At_SignupPage.Company_input.type("My company")

    At_SignupPage.Password_input.type("Test@123")

    At_SignupPage.Confirm_password_input.type("Test@123")

    At_SignupPage.Term_check_box.set_checked(True)

    # At_SignupPage.Submit_button.screenshot(path="startbutton.png")
    At_SignupPage.Submit_button.hover()
    At_SignupPage.Submit_button.click(button="left")
    page.screenshot(path="screenshot.png", full_page=True)
    TestTracing.Stop_Trace_test()




    
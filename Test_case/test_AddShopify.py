from models.Login_page import LoginPage
from Utility.Navigation_Links import Page_links
from Utility.Tracing import Tracing_the_test
from models.Products_dashboard_page import Product_Dashboard
from playwright.sync_api import Page, expect

def test_New_User_Sign_up(page: Page): 
    At_LoginPage= LoginPage(page)
    HomePage=Page_links(page)
    TestTracing= Tracing_the_test(page.context)
    At_ProductPage=Product_Dashboard(page)
    
    TestTracing.Start_Trace_test()
    
    HomePage.navigate()
    At_LoginPage.Sign_in.click()
    At_LoginPage.Email_input.click()
    At_LoginPage.Email_input.fill("isar.petspace@gmail.com")
    At_LoginPage.Password_input.click()
    At_LoginPage.Password_input.fill("Test@123")
    At_LoginPage.Signin_button.click()


    At_ProductPage.Connect_button.click()
    At_ProductPage.Connect_dropdown.select_option("shopify")
    At_ProductPage.Store_input.click()
    At_ProductPage.Store_input.fill("mark1500-qa")
    At_ProductPage.Addchannel_button.click()
    
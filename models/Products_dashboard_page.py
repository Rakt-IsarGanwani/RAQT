from playwright.sync_api import Page

class Product_Dashboard:

    def __init__(self, page:Page):
        self.page = page
        
        self.Connect_button=page.locator("//a[@id='add-sales-channel-button']//img")
        self.Connect_dropdown=page.locator("#id_sales_channel_input")
        #page.locator("#id_sales_channel_input").select_option("square") 
        self.Store_input=page.locator("#shop_url")
        self.Addchannel_button=page.get_by_role("button", name=" Add Channel")
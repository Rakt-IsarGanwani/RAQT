from playwright.sync_api import Page

""""
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    page=browser.new_page()
   
@pytest.fixture(autouse= True, scope= "function")
def Homepage(page:Page):
    
    page.goto("https://staging.quicksync.pro/", timeout=50000)
    page.set_viewport_size({"width": 1366, "height": 768}) 
    return page
     """

class Page_links:
    def __init__(self, page:Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://staging.quicksync.pro/", timeout=50000)
        self.page.set_viewport_size({"width": 1366, "height": 768}) 
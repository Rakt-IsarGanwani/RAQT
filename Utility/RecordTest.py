from playwright.sync_api import  Browser

class Record_test:

 def record_page(self, browser: Browser):
    self.context=browser.new_context(
        record_video_dir="video/"
    )
    self.page=self.context.new_page()

 def close_context(self, browser: Browser):
    self.context.close()
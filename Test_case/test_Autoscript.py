from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://staging.quicksync.pro/")
    page.get_by_text("Live Chat Now").click()
    page.get_by_role("link", name="Privacy Policy").click()
    


#  first actevate Scripts\activate
  #  playwright codegen staging.quicksync.pro   
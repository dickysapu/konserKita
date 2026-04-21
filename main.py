from playwright.sync_api import sync_playwright

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False)
   page = browser.new_page()

   page.goto("https://thesoundsproject.com/ticket")
   print(page.title())

   # button buy tickets
   page.get_by_role("link",name="Buy Tickets").nth(4).click()
   page.get_by_role("link", name="Presale 2 (Day 2 - 8th August) Rp").click()
   page.locator("iframe[name=\"mt-white-label\"]").content_frame.get_by_role("button", name="+").nth(2).click()


   page.wait_for_timeout(5000)
   browser.close()
from playwright.async_api import async_playwright

class PlaywrightService:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start_browser(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True
        )
        self.page = await self.browser.new_page( 
            viewport={"width": 1280, "height": 720}
        )

    async def navigate_page(self, url: str):
        if self.page is None:
            raise Exception("Browser not started. Call start_browser() first.")
        await self.page.goto(url)

    async def get_page(self):
        return self.page
    
    async def close_browser(self):
        if self.browser is not None:
            await self.browser.close()
        if self.playwright is not None:
            await self.playwright.stop()
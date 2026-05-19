import asyncio
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from playwright.async_api import async_playwright

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

playwright = None
browser = None
page = None


@asynccontextmanager
async def lifespan(app: FastAPI):

    global playwright
    global browser
    global page

    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch(
        headless=True
    )

    page = await browser.new_page()

    await page.goto("https://playwright.dev")

    yield

    await browser.close()
    await playwright.stop()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/screenshot")
async def get_screenshot():

    screenshot = await page.screenshot(
        type="png",
        full_page=True
    )

    return Response(
        content=screenshot,
        media_type="image/png"
    )


@app.get("/buttons")
async def get_buttons():

    buttons = page.get_by_role("button")

    count = await buttons.count()

    result = []

    for i in range(count):

        button = buttons.nth(i)

        result.append({
            "text": await button.inner_text(),
            "id": await button.get_attribute("id"),
            "class": await button.get_attribute("class"),
        })

    return result


@app.post("/click")
async def click(data: dict):

    await page.get_by_role(
        "button",
        name=data["name"]
    ).click()

    return {"status": "clicked"}

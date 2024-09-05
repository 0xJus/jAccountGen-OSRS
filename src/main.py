import asyncio
import nodriver as uc
import time

import random
import string
import logging


months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]


async def main():
    # Start the browser
    driver = await uc.start()

    # Open the webpage
    page = await driver.get("https://account.jagex.com/en-GB")

    # need to verify cloudflare

    # let's handle the cookie nag as well
    cookie_bar_accept = await page.find("Allow all cookies", best_match=True)
    if cookie_bar_accept:
        await cookie_bar_accept.click()

    time.sleep(10)

    # # Click "Create an account"
    # create_account = await page.find("Create an account", best_match=True)
    # if create_account:
    #     await create_account.click()

    # # Enter email
    # email = await page.select("input[type=email]")
    # randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))
    # await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

    # # Find and fill in the date of birth fields (assuming they are select elements)
    # print('finding the "month", "day", and "year" select elements')
    # sel_month = await page.find("DD", best_match=True)

    # print('filling in the "password" input field')
    # await password.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

    # # Close the browser
    # await browser.close()


if __name__ == "__main__":
    uc.loop().run_until_complete(main())

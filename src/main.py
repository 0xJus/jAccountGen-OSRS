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
    verify_cloudflare = await page.select("input[type=checkbox]")
    if verify_cloudflare:
        await verify_cloudflare.click()

    # let's handle the cookie nag as well
    cookie_bar_accept = await page.find("Allow all cookies", best_match=True)
    if cookie_bar_accept:
        await cookie_bar_accept.click()

    time.sleep(2)

    # Click "Create an account"
    create_account = await page.find("Create an account", best_match=True)
    if create_account:
        await create_account.click()

    time.sleep(2)

    # Enter email
    email = await page.select("input[type=email]")
    randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))
    await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

    time.sleep(2)

    # Generate random values
    random_month = random.randint(1, 12)
    random_day = random.randint(
        1, 31
    )  # Adjust if you want to consider the number of days in each month
    random_year = random.randint(1990, 2001)

    # Format values
    random_month_str = str(random_month).zfill(2)
    random_day_str = str(random_day).zfill(2)
    random_year_str = str(random_year)

    print('finding the "month", "day", and "year" select elements')

    # Look for the month, day, and year input fields using their name attributes
    sel_day = await page.query_selector('input[name="day"]')
    await sel_day.send_keys(random_day_str)

    sel_month = await page.query_selector('input[name="month"]')
    await sel_month.send_keys(random_month_str)

    sel_year = await page.query_selector('input[name="year"]')
    await sel_year.send_keys(random_year_str)

    time.sleep(3)

    email = await page.select("input[type=email]")
    randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))
    await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

    time.sleep(5)

    # # Look for the element with the specified ID

    # tos_agreement_checkbox = await page.query_selector(
    #     'input[name="registration-start-accept-agreements"]'
    # )

    # # Click the element
    # await tos_agreement_checkbox.click()


# print('filling in the "password" input field')
# await password.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

# # Close the browser
# await browser.close()


if __name__ == "__main__":
    uc.loop().run_until_complete(main())

import asyncio
import nodriver as uc
import time

import random
import string
import logging


async def main():

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

    # Start the browser
    driver = await uc.start()

    # Open the webpage
    page = await driver.get("https://account.jagex.com/en-GB")

    # need to verify cloudflare
    # let's handle the cookie nag as well
    verify_cloudflare = await page.query_selector("button")
    if verify_cloudflare:
        await verify_cloudflare.click()

    # let's handle the cookie nag as well
    cookie_bar_accept = await page.find("Allow all cookies", best_match=True)
    if cookie_bar_accept:
        await cookie_bar_accept.click()

    # Click "Create an account"
    create_account = await page.find("Create an account", best_match=True)
    if create_account:
        await create_account.click()

    # Enter email
    email = await page.select("input[type=email]")
    if email:
        randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))
        await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

    print('finding the "month", "day", and "year" select elements')

    # Look for the month, day, and year input fields using their name attributes
    sel_day = await page.query_selector('input[name="day"]')
    if sel_day:
        await sel_day.send_keys(random_day_str)

    sel_month = await page.query_selector('input[name="month"]')
    if sel_month:
        await sel_month.send_keys(random_month_str)

    sel_year = await page.query_selector('input[name="year"]')
    if sel_year:
        await sel_year.send_keys(random_year_str)

    # Look for the tos & agreement polocies with the specified ID
    # Then find and click the element
    tos_agreement_checkbox = await page.query_selector(
        "#registration-start-accept-agreements"
    )
    if tos_agreement_checkbox:
        await tos_agreement_checkbox.click()

    # Look for the continue button and click it
    continue_button = await page.find("Continue", best_match=True)
    if continue_button:
        await continue_button.click()

    # Sleep for 5 seconds manually
    time.sleep(5)


# START OF VERIFICATION PROCESS
async def verification_process():
    loggin.info("Starting verification process")
    # need to log into gmail and collect verify code
    # display it by either a discord webhook or return the verification code after viewing/scraping the burner email


# print('filling in the "password" input field')
# await password.send_keys("".join([randstr(8), "@", randstr(8), ".com"]))

# # Close the browser
# await browser.close()


if __name__ == "__main__":
    # since asyncio.run never worked (for me)
    # i use
    uc.loop().run_until_complete(main())

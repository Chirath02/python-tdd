from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes
# to checkk out its hompage

browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists

assert 'To-Do' in browser.title

# She is invited to enter a to-do item straigt away

# She types "Buy peakcock feathers" into a text box

# when she hits enter, the page updates, and now the page lists
# '1. Buy peakcoack feathers" as a to-do item

# There is still a text box inviting her to add another item,
# She enters "Use peakcoak feathers to make a fly"

# The page updates, and now shows both the items

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()

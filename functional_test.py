from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to checkk out its hompage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists

        assert 'To-Do' in self.browser.title
        self.fail('Finish the test!')

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

if __name__ == '__main__':
    unittest.main()


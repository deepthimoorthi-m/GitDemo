from hamcrest import *


class BaseAssertions:

    def assertElementPresentByXPATH(self, xpath):
        assert_that(self.driver.getElementTextByXpath(xpath), not_(raises(Exception)))

    def assertElementPresentByCSS(self, locator):
        assert_that((self.driver.isElementPresentByCSS(locator)), is_(True),
                    f"Element by locator {str(locator)} is not present on page.")

    def assertElementNotPresentByCSS(self, locator):
        assert_that((self.driver.isElementPresentByCSS(locator)), is_(False),
                    f"Element by locator {str(locator)} is present on page.")

    def assertElementNotVisibleByCSS(self, locator):
        assert_that((self.driver.isElementNotVisibleByCSS(locator)), is_(True),
                    f"Element by locator {str(locator)} is not visible on page.")

    def assertElementPresentByLinkText(self, link_text):
        assert_that(self.driver.isElementDisplayedByLinkText(link_text), is_(True))

    def assertElementNotPresentByLinkText(self, link_text):
        assert_that(self.driver.isElementDisplayedByLinkText(link_text), is_(False))

    def assertElementNotPresentByXpath(self, xpath):
        assert_that((self.driver.isElementPresentByXpath(xpath)), is_(False),
                    f"Element by xpath {str(xpath)} is present on page.")

    def assertElementNotVisibleByXpath(self, xpath):
        assert_that((self.driver.isElementDisplayedByXPath(xpath)), is_(False),
                    f"Element by xpath {str(xpath)} is visible on page.")

    def assertElementVisibleByXpath(self, xpath, element=''):
        assert_that((self.driver.isElementDisplayedByXPath(xpath)), is_(True),
                    "Element '{element}' by xpath {str(xpath)} is not visible on page.")
        self.log.info(f"Element '{element}' by xpath {str(xpath)} is visible on page.")

    def assertLabelPresentByCSS(self, label, locator):
        assert_that((self.driver.isTextPresentByCSS(label, locator)), is_(True))

    def assertLabelPresentByXpath(self, label, locator):
        assert_that((self.driver.isTextPresentByXpath(label, locator)), is_(True))

    def assertLabelLowerPresentByXpath(self, label, locator):
        assert_that((self.driver.isTextLowerPresentByXpath(label, locator)), is_(True))

    def assertElementPresentByXpath(self, xpath):
        assert_that((self.driver.isElementPresentByXpath(xpath)), is_(True),
                    f"Element by locator {str(xpath)} is not present on page.")

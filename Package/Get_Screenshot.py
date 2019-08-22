# coding = utf - 8
"""手机截图"""


def add_img(self):
    self.imgs.append(self.driver.get_screenshot_as_base64())
    return True

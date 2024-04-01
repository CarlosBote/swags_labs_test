from appium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver(platform):
        if platform.lower() == 'ios':
            desired_caps = {
                'platformName': 'iOS',
                'platformVersion': '13.0',
                'deviceName': 'iPhone 12',
                'automationName': 'XCUITest',
                'app': '../apps/ios/SauceLabsMobileSample2.7.1.ipa'
            }
        elif platform.lower() == 'android':
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '11.0',
                'deviceName': 'Android Emulator',
                'automationName': 'UiAutomator2',
                'app': '../apps/android/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'
            }
        else:
            raise ValueError(f"Platform not supported: {platform}")

        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
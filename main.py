from selenium import webdriver
from time import sleep
import pandas as pd

table = []


class DeansListScraper:

    data = []
    list_honors = []
    list_students = []
    list_gradyear = []
    list_major = []

    def __init__(self):
        self.driver = webdriver.Firefox()

    def data_scrape(self):
        for pageIndex in range(680):
            self.driver.get(
                'https://www.umass.edu/registrar/students/deans-list?page='+str(pageIndex))
            for table in self.driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div[3]/table/tbody/tr'):
                self.data.append([item.text for item in table.find_elements_by_xpath(
                    ".//*[self::td or self::th]")])
        for item in self.data:
            self.list_honors.append(item[0])
            self.list_students.append(item[1])
            self.list_gradyear.append(item[2])
            self.list_major.append(item[3])

    def data_storage(self):
        print(self.list_students)
        self.data = {
            'Honors': self.list_honors,
            'Student': self.list_students,
            'Graduation Year': self.list_gradyear,
            'Major (Degree)': self.list_major
        }
        table = pd.DataFrame(self.data)
        table.to_excel("Dean's List.xlsx", sheet_name="Listed")

    def close_browser(self):
        self.driver.quit()


my_bot = DeansListScraper()
my_bot.data_scrape()
my_bot.data_storage()
my_bot.close_browser()

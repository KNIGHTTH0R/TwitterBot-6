from urllib.request import urlopen
from bs4 import BeautifulSoup
import tweepy
from selenium import webdriver
import time


class scrap:
    def __init__(self, website):
        self.website = website
        self.driver = webdriver.Chrome("./chromedriver")
        self.url = ""
        if self.website is "reuters":
            self.reuters()

    def reuters(self):
        self.driver.get("https://www.reuters.com/")
        self.driver.find_element_by_class_name("edition-arrow").click()
        self.driver.find_element_by_xpath(
            "//a[@href='//www.reuters.com']").click()
        time.sleep(2)
        # next4 = ["//*[@id='hp-top-news-top']/section/div/article[" + str(i) + "]/div/a/h3" for i in range(1, 5)]
        # next10 = ["//*[@id='mCSB_1_container']/li[" + str(i) + "]/h3" for i in range(1, 5)]
        all = "//*[@id='topStory']/section/div[2]/h2"
        # all.extend(next4)
        # all.extend(next10)
        # for i in all:
        try:
            time.sleep(7)
            self.driver.find_element_by_xpath(all).click()
            time.sleep(2)
            a = self.driver.find_elements_by_tag_name("p")
            title = self.driver.find_element_by_class_name(
                "ArticleHeader_headline").text
        except:
            pass
        story = ""
        for i in a:
            story += i.text
        self.filewriting(story, title, "reuters")
        self.url = self.driver.current_url
        # self.driver.execute_script("window.history.go(-1)")
        self.driver.quit()
        

        
    
    def filewriting(self, web, title, loc):
        with open(loc + ":" + title, "w") as file:
            file.write(web)


    def tweeting(self):
        auth = tweepy.OAuthHandler('GVBkhXef34jiNz1oeycazCx8I','3iIBGIBH8UkbRUFWfIesPajIl4lISwx0lfFAWrVqXntnIPdmcK')
        auth.set_access_token('1237336099854245888-RRROxzaiyzWk6T0mcwdxjWVjOBCVO5', 't9SMF1voUWsaebmgw0uTTulCviXy2XvRQw0R5HX3IDupQ')
        api = tweepy.API(auth)
        api.update_status("This is my first tweet!")
scrap("reuters")



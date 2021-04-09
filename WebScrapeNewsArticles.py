from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from openpyxl import Workbook

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#searchterm=input()
driver.get("https://www.reuters.com/")
driver.find_element_by_class_name('search-icon').click()
searchelem = driver.find_element_by_id('searchfield')
searchelem.send_keys('sex work')
searchelem.send_keys(Keys.ENTER)
k = driver.find_element_by_class_name('search-result-list')
links = k.find_elements_by_xpath(
    "//div[@class='search-result-indiv']//div[@class='search-result-content']//h3[@class='search-result-title']//a[contains(@href,'')]")
links1 = []
for link in links:
    links1.append(link.get_attribute("href"))
li = []
for link in links1:
    dict1 = {}
    dict1['url'] = link
    driver.get(link)
    date = driver.find_element_by_xpath(
        "//div[@class='ArticleHeader-date-line-3oc3Y']//time[@class='TextLabel__text-label___3oCVw TextLabel__gray___1V4fk TextLabel__small-all-caps___2Z2RG ArticleHeader-date-Goy3y']").text
    print(date)
    title = driver.find_element_by_xpath(
        "//div[@class='ArticlePage-article-header-23J2O']//h1[@class='Headline-headline-2FXIq Headline-black-OogpV ArticleHeader-headline-NlAqj']").text
    print(title)
    #author=driver.find_element_by_xpath("//div[@class='ArticleBody-byline-container-3H6dy']//p[@class='Byline-byline-1sVmo ArticleBody-byline-10B7D']//span[@class='TextLabel__text-label___3oCVw TextLabel__black-to-orange___23uc0 TextLabel__serif___3lOpX Byline-author-2BSir __web-inspector-hide-shortcut__']").text
    #print(author)
    dict1['date'] = date

    dict1['title'] = title
    #dict1['author']=author
    li.append(dict1)
#print(li)
df=pd.DataFrame(li)
excel=input("Enter the path to stored in")
path=excel+'/output.xlsx'
df.to_excel(path, index = False)
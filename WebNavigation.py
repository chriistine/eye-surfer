from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




def search_for_news(topic, driver):

    searchBtn = driver.find_element_by_class_name("top-menu-search__button")
    searchBtn.click()

    inputElement = driver.find_element_by_css_selector('input[name=search_text]')

    inputElement.send_keys(topic)
    inputElement.send_keys(Keys.ENTER)

    # return list of articles on the first page
    articleHeaders = []
    time.sleep(2)

    # gets the link

    articleHeaders = driver.find_elements_by_class_name("article-card__link")
    titles = [articleHeader.text for articleHeader in articleHeaders]
    links = [articleHeader.get_attribute('href') for articleHeader in articleHeaders]
    #for link in links:
    #    print(link)
    #print(len(links))
    for i in range(len(titles)):
        titles[i] = titles[i].split("\n")[0]
        
    title_link_data = {}

    i = 0
    for title, link in zip(titles, links):
        entry = [title, link]
        title_link_data[i] = entry
        i += 1
    
    #print(title_link_data)
    return title_link_data




def select_news(title_link_data, selected_news_int, driver):
    # 0 being the first article
    
    href = title_link_data[selected_news_int][1]
    driver.get(href)

    contents = driver.find_elements_by_class_name('article-content__content-group')
    article = ""
    for content in contents:
        refined_content = content.find_elements_by_css_selector('p')
        for refined in refined_content:
            article = article + refined.text

    article_list = []
    if len(article) > 4500:
        article = split_article(article)
        return article
    else:
        article_list.append(article) 
        return article_list
    
def split_article(article):
    mid_char_index = int(len(article)/2)
    #print(mid_char_index)
    split_index = 0
    split_string = []
    for i in range(0, mid_char_index):
        if article[i + mid_char_index - 1] == '.' and ((article[i + mid_char_index] == ' ') or (article[i + mid_char_index].isupper())):
            split_index = i + mid_char_index
            #print(split_index)
            break
    
    split_string.append(article[:split_index])
    split_string.append(article[split_index:])

    return split_string


def main():
    driver = webdriver.Chrome(r'C:\Users\danie\dev\deltahacks\deltahacks2021\chromedriver.exe')

    driver.get('https://nationalpost.com/')
    data = search_for_news("vaccine", driver)
    article = select_news(data, 0, driver)
    #split_article(article)



if __name__ == "__main__":
    main()

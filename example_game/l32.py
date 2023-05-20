from bs4 import BeautifulSoup
import lxml
"""with open("C:/Users/User/PycharmProjects/example_game/index.html") as page:
    soupchik = BeautifulSoup(page, 'lxml')
    #tag_div = soupchik.find('div')
    tag_p = soupchik.find_all('p')
    #print(tag_div)
for i in range(len(tag_p)):
    print(i, tag_p)"""


with open("skidki.html.", encoding='utf-8') as page:
    soupchik = BeautifulSoup(page, 'lxml')
    tag_a = soupchik.find_all('div', class_='ImpressionTrackedElement')

#print(tag_a)
for game in tag_a:
    name =  game.find('div', class_='salepreviewwidgets_StoreSaleWidgetTitle_3jI46')
    name_1 = str(name).rstrip('>')
    #print(name)
    if name == None:
        pass
    else:
        print(name.text)
    #link = game.find('a', class_='capsule header' )#class_='salepreviewwidgets_StoreSaleWidgetTitle_3jI46')
    #print(link)
    # if link == None:
    #     pass
    # else:
    #     print(link)

    # link = game.get('href')
    # print(link)
    

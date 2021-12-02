import requests
from bs4 import BeautifulSoup

url_home = 'https://www.pagina12.com.ar'

def get_links_from_sections(content):
    s=BeautifulSoup(content.text, 'lxml')
    articles=s.find_all('article')
    article_links=[]
    for article_temp in articles:
        article_links.append(url_home+article_temp.find('a').get('href'))
    return article_links

def get_sections_from_home(content):
    s = BeautifulSoup(content.text, 'lxml')
    secciones =(s.find('ul',attrs={'class', 'horizontal-list main-sections hide-on-dropdown'}).find_all('li'))
    return [seccion.a.get('href') for seccion in secciones ]
    

def main():
    p12 = requests.get(url_home)
    links_secciones =  get_sections_from_home(p12)
    article_links=[]
    print('--------------------------------------\n')
    for link_temp in links_secciones:
        temp_content=requests.get(link_temp)
        article_links= article_links+ get_links_from_sections(temp_content)

        print(article_links)    
        print('--------------------------------------\n')

if __name__ == "__main__":
    main()
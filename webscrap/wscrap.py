from bs4 import BeautifulSoup
from urllib.request import urlopen



filepath = "html_data/aj.html"


class GetScrapper:

    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self, url, wlog):
        self.__url = url
        self.__wlog = wlog

    def GetWebPage(self):

        try:
            html = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data = html.read()
            if len(self.__data)>0:
                print("Successful")
                return self.__data
            # print(self.__data)

    def write_data_into_html(self, filepath = filepath, data=''):
        try:
            with open(filepath, 'wb') as store:
                if data:
                    store.write(data)
                else:
                    store.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(e)

    # def read_data_from_html(self, filepath = filepath):
    #     try:
    #         with open(filepath) as r:
    #             self.__data = r.read()
    #     except Exception as e:
    #         print(e)
    #         self.__wlog.report(e);


    def convert_data_to_beautifulsoup(self):
        self.__soup = BeautifulSoup(self.__data, "html.parser")
        return self.__soup

    def modify_data(self):
        # data_list = self.__soup.find_all(['p'], class_='content-img')
        data_list = self.__soup.find_all('h4', class_='pad-bottom-small')


        html_text = '''
        <html>
        
        <head><title>Daily Star Scrapper</title></head>
        <body>
        {NEWS_LINKS}
        </body>
        </html>
        '''
        news_link = '<ol>'
        for tags in data_list:
            # print(tags.a['href'])
            
            if tags.a['href']:
                link = 'https://www.thedailystar.net' + tags.a['href']

                title = tags.a.string

                news_link += "<li><a href='{}' target='_blank'>'{}'</li>\n".format(link, title)

        news_link += '</ol>'

        html_text = html_text.format(NEWS_LINKS=news_link)

        self.write_data_into_html(filepath = 'html_data/news.html', data = html_text.encode())
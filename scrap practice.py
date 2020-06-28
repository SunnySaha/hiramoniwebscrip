from webscrap import weblog
from webscrap import wscrap


url_demo = "https://www.thedailystar.net/tags/rape-bangladesh"


g = wscrap.GetScrapper(url_demo, weblog)

f = g.GetWebPage()
g.write_data_into_html()
#g.read_data_from_html()
convert = g.convert_data_to_beautifulsoup()
g.modify_data()
print(convert.title.text)





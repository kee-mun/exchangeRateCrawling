import urllib.request
import bs4
from matplotlib import pyplot as plt

url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_JPYKRW"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
daytable_html = bs_obj.find("table")
day_values = daytable_html.find_all("tr")

# print(day_values)
x = []
y = []
changedY = []

for i in range(len(day_values)):
    if i == 0 or i == 1:
        pass
    else:
        date = day_values[i].find("td", class_="date").contents[0]
        rate_ = day_values[i].find("td", class_="num").contents[0]
        x.append(date)
        print(date)
        rate = ""
        for i in rate_:
            if i == ",":
                pass
            else:
                rate += i
        y.append(float(rate))

x.reverse()
y.reverse()

plt.figure(figsize=(15,5))
plt.plot(x, y)
plt.show()
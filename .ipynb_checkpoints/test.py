from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests


URL = 'https://www.amazon.com/Best-Sellers/zgbs'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
          'referer': 'https://www.amazon.com/'}
html = requests.get(URL, headers=header)

soup = BeautifulSoup(html.content, 'html.parser')

category = soup.find("div", attrs={
                'class': 'p13n-zg-nav-tree-all_style_zg-browse-item1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-small_nleKL'})

categoryNames = list()
categoryLinks = list()

for name in category:
    categoryNames.append(name.get_text())

for atrr in category:
    print(atrr.attrs)


df = pd.DataFrame({"Category": categoryNames})
#print(df)

import  random,requests
from bs4 import BeautifulSoup
def Get_text(): #从新浪新闻官网获取分析文本
    url = 'https://news.sina.com.cn/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
         }
    soup = BeautifulSoup(requests.get(url,headers = headers).text,'html.parser')
    ul_soup = soup.find_all(class_='ct_t_01')
    href_list=[]
    for ul in ul_soup:
        li_soup = ul.find_all(name='h1' )
        for li in list(li_soup):
            a_soup = li.find_all(name='a')
            for a in a_soup:
                href_list.append(a['href'])
    # print('文本来自新浪新闻')
    # print(random.sample(href_list,1))
    html = requests.get(random.sample(href_list,1)[0],headers = headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'html.parser')
    Article = soup.find_all(class_='article')
    p_tags = Article[0].find_all(name = 'p')
    text = ''
    for p in p_tags:
        text = text + p.get_text()
    return text

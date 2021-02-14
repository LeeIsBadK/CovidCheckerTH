import requests
import time
from bs4 import BeautifulSoup


url = "https://ddc.moph.go.th/viralpneumonia/index.php"
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text, 'html.parser')
find_word = soup.find_all("h4",{"class":"txt"})

time_now = time.asctime(time.localtime(time.time()))

word = []
for i in find_word:
    i = str(i).split('<h4 class="txt">')[1]
    i = str(i).split('</h4>')[0]
    word.append(i)


print('รายงานยอดผู้ติดเชื้อ Covid-19 ในไทย')
print(f'ยอดผู้ติดเชื้อรายใหม่ {word[1]} ราย')
print(f'ยอดผู้เสียชีวิต {word[2]} ราย')
print(f'ยอกผู้เติดเชื้อสะสม {word[0]} ราย\n')

print(f'ที่มา : {url}')
print(time_now)
input()

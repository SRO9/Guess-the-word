import requests as req
from string import ascii_letters
url = 'https://britlex.ru/5000words.php'
site = req.get(url)
text = site.text

lst = text.split('\n')
res_lst = []
for i in lst:
    w = ''
    if '<tr>' in i:
        for letters in i:
            if letters in ascii_letters + '</>':
                w += letters
    res_lst.append(w)


for i in range(len(res_lst)):
    res_lst[i] = res_lst[i][17: len(res_lst[i]) - 28]

lst_words = [i for i in res_lst if i != '' and ('<(' not in i)]


'''
WORK IN PROGRESS

'''


import requests
from bs4 import BeautifulSoup

#replace the string with a real website link to test it
sitemap = 'http://www.websitelinkexample.com'

rec = requests.get(sitemap)
html = rec.content

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
urls = [link.get('href') for link in links
        if link.get('href') and link.get('href')[0:4]=='http']

results = []
for i, url in enumerate(urls,1):
    try:
        rec = requests.get(url)
        report = str(rec.status_code)
        if rec.history:
            history_status_codes = [str(h.status_code) for h in rec.history]
            report += ' [HISTORY: ' + ', '.join(history_status_codes) + ']'
            result = (rec.status_code, rec.history, url, 'No error. Redirect to ' + rec.url)
        elif rec.status_code == 200:
            result = (rec.status_code, rec.history, url, 'No error. No redirect.')
        else:
            result = (rec.status_code, rec.history, url, 'Error?')
    except Exception as e:
        result = (0, [], url, e)
        
    results.append(result)

# first Sort by status then history length
results.sort(key=lambda result:(result[0],len(result[1])))

print('301s')
i = 0
for result in results:
    if len(result[1]):
        i += 1
        print(i, end='. ')
        for response in result[1]:
            print('>>', response.url, end='\n\t')
        print('>>>>',result[3])
        
#non-200s
print('\n==========\nERRORS')
for result in results:
    if result[0] != 200:
        print(result[0], '-', result[2])
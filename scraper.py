import requests, scraperwiki

# JSON file provided by the Swiss Federal Office of Statistics
# Source: https://www.experimental.bfs.admin.ch/expstat/en/home/innovative-methods/swisscovid-app-monitoring.assetdetail.13428386.html
url = "https://www.bfs.admin.ch/bfsstatic/dam/assets/orderNr:ds-q-14.01-SwissCovidApp-01/master"

r = requests.get(url) #, verify=False)

if r.status_code != 200:
    print('Error', r.status_code, r.text)
    exit()

data = r.json()
print('Updating', data['dataStatus'])

# Save to database
scraperwiki.sqlite.save(unique_keys=['Date'], data=data['data'])
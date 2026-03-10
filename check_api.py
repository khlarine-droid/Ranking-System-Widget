import urllib.request, json
url='https://opensheet.elk.sh/1ZynLl7nNSC9UiFOcoq3X1uGwndaVLvn1x5WRa-NfB6Y/Providers%20with%20actual%20reviews%20and%20ranking'
with urllib.request.urlopen(url) as r:
    data=json.load(r)
print('count',len(data))
print(data[0])
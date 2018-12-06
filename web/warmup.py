import urllib2
ans = ""
for i in range(100):
    url = 'http://104.199.235.135:31331/index.php?p=' + str(i)
    response = urllib2.urlopen(url)
    r = str(response.info())
    ans += r[108].replace("\r"," ")
    if r[108] == "}":
        print(ans)
        break

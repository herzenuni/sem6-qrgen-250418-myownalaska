import pyqrcode
url = pyqrcode.create('https://www.herzen.spb.ru/')
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))
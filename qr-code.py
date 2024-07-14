import pyqrcode

my_url = 'www.google.com'
url = pyqrcode.create(my_url)

url.svg("connect with me")
url.png("connect with me")
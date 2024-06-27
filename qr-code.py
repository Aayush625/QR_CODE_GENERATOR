import pyqrcode

my_url = 'https://www.linkedin.com/in/aayush-sinha-97b425240/'
url = pyqrcode.create(my_url)

url.svg("connect with me")
url.png("connect with me")
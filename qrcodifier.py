import urllib.parse
import base64
import requests


api_url = 'https://chart.googleapis.com/chart?'

with open('logo.png', 'rb') as f:
    photo = base64.b64encode(f.read())
full_name = ''
organization = ''
phone = '+1'
url = ''
email = ''
address1 = ''
address2 = ''
city = ''
state = ''
zip_code = ''
country = ''
full_address = f'{address1} {address2} {city}, {state} {zip_code}, {country}'
notes = ''

query = {'chs': '400x400','cht': 'qr', 'chl': f"""BEGIN:VCARD
VERSION:4.0
PRODID:-//Apple Inc.//iPhone OS 12.3.1//EN
N: {full_name}
ORG: {organization}
TEL: {phone}
PHOTO;ENCODING=BASE64;TYPE=PNG:{photo.decode('utf-8')}
URL: {url}
EMAIL: {email}
ADR: {full_address}
NOTE: {notes}
END:VCARD
"""}

url_encode_query = urllib.parse.urlencode(query)
final_url = api_url + url_encode_query

with open('qrcode.png', 'wb') as f:
    f.write(requests.get(final_url).content)
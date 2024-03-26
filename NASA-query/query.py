import urllib
import requests


url = "https://images-api.nasa.gov/search?q=ilan ramon"
response = requests.get(url)
response.raise_for_status()

collection = response.json()['collection']
sum = 0
next_page = True
while next_page:
    if collection['links'][0]['rel'] == 'prev':
        next_page = False
    next_page_url = collection['links'][0]['href']

    jsondict = collection['items']

    print(F"the size isss: {len(jsondict)}")

    for i in range(len(jsondict)):
        print(i)
        image_url = requests.get(jsondict[i]['href']).json()

        orig_image_url = image_url[0]

        image_response = requests.get(orig_image_url)

        content_length = urllib.request.urlopen(orig_image_url).headers.get('Content-Length')
        if int(content_length) / 1000 >= 1000:
            sum += 1

    response = requests.get(next_page_url)
    response.raise_for_status()
    collection = response.json()['collection']

print(f"sum = {sum}")

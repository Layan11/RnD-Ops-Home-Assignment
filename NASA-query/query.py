import urllib
import requests
import csv

"""
This is a script in python which queries the NASA image and video library for all assets related to “Ilan Ramon”.
And from the results creates a CSV file, named 'output.csv', containing Nasa_id and file size in kb for all images 
with original file size larger than 1000 kb.
"""


# given a dictionary of images and an index, returns the size of the corresponding image in kb
def get_size_in_kb(jsondict, index):
    # gets the url of the image file in different sizes (small, medium, large, and original) as well as metadata
    image_urls = requests.get(jsondict[i]['href']).json()
    # get the url for the image in the original size, which is in index 0 of the image_urls list
    orig_image_url = image_urls[0]

    # the urlopen request returns an http response, then retrieve the content
    # length from the 'Content-Length' header, which has the image file size in bytes
    content_length = urllib.request.urlopen(orig_image_url).headers.get('Content-Length')
    image_size_in_kb = int(content_length) / 1024

    return image_size_in_kb

#??????
def get_collection(url):
    # get request for the given url
    response = requests.get(url)
    # raise exception in case there was an error during the get request
    response.raise_for_status()
    # ???????
    collection = response.json()['collection']

    return collection


# creates a csv file with the given list of rows
def create_csv_output(output_rows_list):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Nasa_id", "size_in_kb"]
        writer.writerow(field)
        for row in output_rows_list:
            writer.writerow(row)


# this is nasa's api endpoint to perform a search
url = "https://images-api.nasa.gov/search?q=ilan ramon"
collection = get_collection(url)
output_rows_list = []
next_page = True

# there could be multiple pages in the get response, so this while loop keeps running while there is a next page
# to go through all the pages
while next_page:
    # checks if there is a next page
    if collection['links'][0]['rel'] == 'prev':
        next_page = False

    # get the next page url to go through its images in the next iteration
    next_page_url = collection['links'][0]['href']
    # the 'jsondict' is a dictionary that has all the images information and metadata
    jsondict = collection['items']

    # goes over all the images in the 'jsondict'
    for i in range(len(jsondict)):
        # get the current image size in kb
        image_size_in_kb = get_size_in_kb(jsondict, i)

        if image_size_in_kb > 1000:
            nasa_id = jsondict[i]['data'][0]['nasa_id']
            output_rows_list.append([nasa_id, image_size_in_kb])

    # update the collection to the collection of the next page
    collection = get_collection(next_page_url)

# write a csv output file with the nasa id and the image size in kb for all images with file size bigger than 1000 kb
# which we saved in the list 'output_rows_list'
create_csv_output(output_rows_list)

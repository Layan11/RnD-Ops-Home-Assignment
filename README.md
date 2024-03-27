# RnD-Ops-Home-Assignment

This is a script in python which queries the NASA image and video library for all assets related to “Ilan Ramon”.  
And from the results creates a CSV file, named 'output.csv', containing Nasa_id and file size in kb for all images 
with original file size larger than 1000 kb.  

The script uses REST API, specifically the GET request in order to interact with NASA's API and retrieve some data from NASA's image and video library, it then filters the results and keeps only the data which matches the query's purpose, which is images with original file size larger than 1000 kb, and then saves some of the details from this data to a csv file.  

In order to clone this repository you need to copy and paste this url:  'https://github.com/Layan11/RnD-home-test.git'  

The packages you need to import to be able to run the script are the following packages:  
'import urllib'  
'import requests'  
'import csv'  

To run the script use the 'python query.py' command.  
After the script finishes running, it will create a csv output file named 'output.csv' which will contain all of the query's output in a table.

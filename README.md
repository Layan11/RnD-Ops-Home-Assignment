# RnD-Ops-Home-Assignment

This is a script in python which queries the NASA image and video library for all assets related to “Ilan Ramon”.  
And from the results creates a CSV file, named 'output.csv', containing Nasa_id and file size in kb for all images 
with original file size larger than 1000 kb.  

The script uses REST API, specifically the GET request in order to interact with NASA's API and retrieve some data from NASA's image and video library, it then filters the results and keeps only the data which matches the query's purpose, which is images with original file size larger than 1000 kb, and then saves some of the details from this data to a csv file.  

## Running Instructions:
### 1. Python3:
Make sure you have Python3 installed on your machine, if not, you can use the link below:  
'https://www.python.org/downloads/'  

### 2. Cloning the repository:  
In order to clone, run this from cmd:  
'git clone https://github.com/Layan11/RnD-Ops-Home-Assignment.git'   

### 3. Installing packages:
You need to install packages to be able to run the script, the packages are in Requirements.txt file.  
Run this command line to install:  
'pip install -r Requirements.txt'   

### 4. Run the script:
You are now ready to run the script, to do so, run this from cmd:  
'python query.py'   

### 5. Output:
After the script finishes running, it will create a csv output file named 'output.csv' which will contain all of the query's output in a table.  

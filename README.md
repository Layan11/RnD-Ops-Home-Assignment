# RnD-Ops-Home-Assignment
## Part 1 - NASA query:
This is a script in python which queries the NASA image and video library for all assets related to "Ilan Ramon".  
And from the results creates a CSV file, named 'output.csv', containing Nasa_id and file size in kb for all images 
with original file size larger than 1000 kb.  

The script uses REST API, specifically the GET request in order to interact with NASA's API and retrieve some data from NASA's image and video library, it then filters the results and keeps only the data which matches the query's purpose, which is images with original file size larger than 1000 kb, and then saves some of the details from this data to a csv file.  

The script includes a requirements file which has all the packages you'll need to install, as well as a configurations file which has the api endpoint needed for the query.  

Note: The query asked for related images as well as videos from the NASA library, but since there were no videos related to "ilan ramon" i didn't adress it in the code and assumed that im dealing with images only since i already knew there are no videos included.

## Running Instructions:
### 1. Python3:
Make sure you have Python3 installed on your machine, if not, you can use the link below:  
'<code>https://www.python.org/downloads/</code>'

### 2. Cloning the repository:  
In order to clone, run this from cmd:  
'<code>git clone https://github.com/Layan11/RnD-Ops-Home-Assignment.git</code>'   

### 3. Installing packages:
You need to install packages to be able to run the script, the packages are in Requirements.txt file.  
Run this command line to install:  
'<code>pip install -r Requirements.txt</code>'   

### 4. Run the script:
You are now ready to run the script, to do so, run this from cmd:  
'<code>python query.py</code>'   

### 5. Output:
After the script finishes running, it will create a csv output file named 'output.csv' which will contain all of the query's output in a table.  

## Part 2 - AWS instances
I created and launced an AWS EC2 instance as well as an RDS instance using the AWS console. I attached the RDS instance to the EC2 instance i created, and then used the instance to run the script from part 1 mentioned above.  

Before launching the instances i went through all the different parameters for each instance and configured them myself.  

Here i provide two screenshots to show the running instances, however i made a very detailed pdf file in which i explain all the steps i made to launch them as well as some explanation for the parameters i chose, some screenshots, and screen recordings.  Open this link to see the detailed file:  
''

### <b>Screenshot of the running ec2 instance, named 'ec2-instance':</b>
![Screenshot (522)](https://github.com/Layan11/RnD-Ops-Home-Assignment/assets/82317996/387be04d-bd39-4297-84f1-ccc938909101)

---

### <b>Screenshot of the attached RDS instance, named 'ec2-db-nvirginia':</b>
![Screenshot (511)](https://github.com/Layan11/RnD-Ops-Home-Assignment/assets/82317996/a244b76b-af43-4fb6-90cd-33c8161ec4ac)


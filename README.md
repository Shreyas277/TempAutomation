Here!!
I was working on the project where I need to calculate an hourly temperature-related data of any location on the globe for the entire last year 2023.

Data was scrapped from the https://www.wunderground.com/ website.

As it is cumbersome to click multiple times the same button again and again , the code was written to automate the process.

First of all, Lets look into the requirements.sh . It's bash file which upon execution installs all the necesarry packages.Ensure all the files are in the same directory.

In the first programme final_temp.py , we need to provide the name of the city and state of which data needs to be scrapped.The programme will output the link from where data would be scrapped.

Now taking the link from previous programme as input, we will execute the second python script that's 'Final_Temperature.py'. These file will execute 12 times inside the bash script for 12 different months. The programme loads the 

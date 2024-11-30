Here!!
I was working on the project where I need to calculate an hourly temperature-related data of any location on the globe for the entire last year 2023.
Data was scrapped from the https://www.wunderground.com/ website.
As it is cumbersome to click multiple times the same button again and again , the code was written to automate the process.

First of all, Lets look into the requirements.sh . It's bash file which upon execution installs all the necesarry packages.Ensure all the files are in the same directory.
In the first programme , with the help of given inputs it generated the link for the data and forwards it towards the second programme.
While the second programme scraps the data from the link by loading it for each and every date of the year.

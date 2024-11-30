#!/bin/bash
echo "Enter the city"
read city
echo "Enter the State or Country"
read state

python3 final_temp1.py $city $state > final_url.txt

link=$(cat final_url.txt)

echo $link

python3 final_temp2.py $link


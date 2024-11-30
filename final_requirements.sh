#!/bin/bash
pip install selenium   #installation of the selenium package

#for installing the chromedriver and unziping it
wget https://chromedriver.storage.googleapis.com/$(google-chrome --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | cut -d. -f1-3)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

#for installing the google-chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

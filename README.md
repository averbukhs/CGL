# Selenium Python tests 

## Prerequisites:
 - ubuntu16 (if you want to run test on another linux distribution you will have to find a way to install google chrome)
 - python3 
 - pip3

## Note:
 - if you want to run test on another linux distribution you will have to find a way to install google chrome
 - if should work on windows too, make sure that chromedriver.exe in PATH and latest version

## Prepare environment:
```bash
pip3 install -U selenium
sudo apt-get update
sudo apt-get install -y libappindicator1 fonts-liberation 
cd /tmp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb

wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/local/bin/
```

## Run tests:
```bash
python3 test_home_page.py
```

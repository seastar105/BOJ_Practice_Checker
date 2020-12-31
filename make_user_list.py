import sys
import os
import re
from bs4 import BeautifulSoup
import requests

def main(argc, argv):
    if argc != 2:
        print("Invalid Arguments")
        print("Usage : python3 make_user_list.py [BOJ Group Member URL]")
        sys.exit(-1)
    
    url = argv[1]
    response = requests.get(url)
    if response.status_code != 200:
        print("HTTP Request Fail with {}".format(response.status_code))
        sys.exit(-1)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    script_path = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_path, 'total_user_list.txt')
    f = open(txt_path,'w')
    for div in soup.findAll('div', attrs={'class':'col-xs-6 col-sm-4 col-md-3 member'}):
        f.write(div.find('a').contents[0])
        f.write("\n")
    f.close()
    

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
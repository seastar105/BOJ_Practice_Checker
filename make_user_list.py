import sys
import os
import re
from bs4 import BeautifulSoup
import requests

def main(argc, argv):
    if argc != 2 and argc != 3:
        print("Invalid Arguments")
        print("Usage : python3 make_user_list.py [BOJ Group Member URL] (--no-admin)")
        sys.exit(-1)
    no_admin_flag = False
    if argc == 3:
        if argv[2] != "--no-admin":
            print("Invalid Arguments")
            print("Usage : python3 make_user_list.py [BOJ Group Member URL] (--no-admin)")
            sys.exit(-1)
        no_admin_flag = True
    url = argv[1]
    response = requests.get(url)
    if response.status_code != 200:
        print("HTTP Request Fail with {}".format(response.status_code))
        sys.exit(-1)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    if no_admin_flag:
        soup = soup.find('div', attrs={'class':'row', 'id':'team_member'})
    script_path = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_path, 'total_user_list.txt')
    user_list = []
    f = open(txt_path,'w')
    for div in soup.findAll('div', attrs={'class':'col-xs-6 col-sm-4 col-md-3 member'}):
        user_list.append(div.find('a').contents[0])
    f.write('\n'.join(user_list))
    f.close()
    

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)

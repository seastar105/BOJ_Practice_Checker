import sys
import os
import re
from bs4 import BeautifulSoup

def load_total_user(base_dir):
    try:
        data = open(os.path.join(base_dir, 'total_user_list.txt'))
    except:
        print("No User list")
        print("Run make_user_list.py First")
        sys.exit(-1)
    ret = []
    for user in data:
        ret.append(user)
    return ret

def main(argc, argv):
    if argc != 2:
        print("Invalid Arguments")
        print("Usage : python3 main.py [Local HTML File Name]")
        sys.exit(-1)
    ############################## FILE OPEN ##############################
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_name = argv[1]
    html_path = os.path.join(script_path, file_name)
    try:
        data = open(html_path, encoding='utf-8')
    except:
        print("No File {}".format(html_path))
        print("Script File and HTML File should be in same directory")
        sys.exit(-1)
    #######################################################################
    soup = BeautifulSoup(data, 'html.parser')
    total_user_list = load_total_user(script_path)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
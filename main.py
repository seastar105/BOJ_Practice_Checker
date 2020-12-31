import sys
import os
import re
from bs4 import BeautifulSoup

def main(argc, argv):
    if argc != 2:
        print("Invalid Arguments")
        print("Usage : python3 main.py [Local HTML File Name]")
        sys.exit(-1)
    ############################ FILE OPEN ################################
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
    

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
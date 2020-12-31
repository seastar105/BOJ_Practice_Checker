import sys
import os
import re
from bs4 import BeautifulSoup

def load_except_user(base_dir):
    ret = list()
    try:
        data = open(os.path.join(base_dir, 'except_user_list.txt'))
    except:
        return ret
    for user in data:
        ret.append(user)
    return ret

def load_total_user(base_dir):
    try:
        data = open(os.path.join(base_dir, 'total_user_list.txt'))
    except:
        print("No User list")
        print("Run make_user_list.py First")
        sys.exit(-1)
    ret = list()
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
    soup = BeautifulSoup(data, 'lxml')
    #######################################################################

    ############################## LOAD USER ##############################
    total_user_list = load_total_user(script_path)
    except_user_list = load_except_user(script_path)
    user_list = [user for user in total_user_list if not in user not in except_user_list]
    #######################################################################
    problem_list = list()
    pattern = re.compile(r'[0-9]{4,5}')
    mhtml_flag = False
    if file_name.find(".mhtml") != -1:
        mhtml_flag = True
    problem_class = "list-group-item"
    if mhtml_flag:
        problem_class = '3D"list-group-item"'
    for div in soup.find_all('li', attrs={'class':problem_class}):
        problem_number = re.search(pattern, div.find('a')['href']).group()
        problem_list.append(problem_number)
    

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
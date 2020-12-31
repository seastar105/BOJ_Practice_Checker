import sys
import os
import re
from bs4 import BeautifulSoup

def load_target_problems(base_dir):
    ret = list()
    try:
        data = open(os.path.join(base_dir, 'target_problem_list.txt'))
    except:
        return ret
    for problem in data:
        ret.append(int(problem))
    return ret

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
    user_list = [user for user in total_user_list if user not in except_user_list]
    #######################################################################

    ############################# PARSE PROBLEMS ##########################
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
    problem_rev_table = dict()
    for i in range(len(problem_list)):
        problem_rev_table[i] = problem_list[i]
    #######################################################################

    ########################## GET ACTIVE USERS ###########################
    target_problems = load_target_problems(script_path)
    if len(target_problems) == 0:
        target_problems = problem_list
    table_id = 'contest_scoreboard'
    if mhtml_flag:
        table_id = '=3D"contest_scoreboard"'
    table = soup.find('table', attrs={'id':table_id}).find('tbody')
    active_user_list = dict()
    accept_class = "accepted"
    if mhtml_flag:
        accept_class = '3D"accepted"'
    for row in table.find_all('tr'):
        user_id = row.find('a').contents[0]
        active_user_list[user_id] = []
        tds = row.find_all('td')
        for i, td in enumerate(tds):
            if td.has_attr('class') and (accept_class in td['class']):
                number = problem_list[i]
                if number in target_problems:
                    active_user_list[user_id].append(number)
    for user in active_user_list:
        print(active_user_list[user])
    #######################################################################

    


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
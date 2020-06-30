import random
import time
import requests
import json
from datetime import datetime

URL = 'https://leetcode.com/api/problems/all/'

if __name__ == '__main__':
    random.seed(time.time())
    r = requests.get(URL)
    resp = r.json()
    num_total = resp['num_total']
    i = random.randint(1, num_total)
    status_pairs = resp['stat_status_pairs']
    result = next(j for j in range(len(status_pairs)) if status_pairs[j]['stat']['frontend_question_id'] == i)
    question = status_pairs[result]
    
    res = ''
    res += question['stat']['question__title'] + '\n\n'
    res += 'Difficulty: ' + str(question['difficulty']['level']) + '\n'
    res += 'Total ACs: ' + str(question['stat']['total_acs']) + '\n'
    res += 'Total Submitted: ' + str(question['stat']['total_submitted']) + '\n'
    res += 'URL: ' + 'https://leetcode.com/problems' + '/' + question['stat']['question__title_slug'] + '\n'
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    f = open("history.txt", "a")
    f.write("\n\n")
    f.write(timestampStr + '\n')
    f.write(res)
    f.close()
    print(res)
    #print('\n\n')
    #print(question['stat']['question__title'] + '\n')
    #print('Difficulty: ' + str(question['difficulty']['level']))
    #print('Total ACs: ' + str(question['stat']['total_acs']))
    #print('Total Submitted: ' + str(question['stat']['total_submitted']))
    #print('URL: ' + 'https://leetcode.com/problems' + '/' + question['stat']['question__title_slug'])


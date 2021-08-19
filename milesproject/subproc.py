from subprocess import Popen, PIPE
import time
import pandas as pd

def evaluate():
    count = 0
    queries = []
    responses = []
    times = []
    with open('/home/milesproject2021/Teacher_text_tokens.txt', 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            print('Query : {}'.format(line))
            queries.append(line)
            start_time = time.time()
            process = Popen(['/usr/bin/python3', '/home/milesproject2021/chatbot.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate(input=line.encode())
            response = stdout.split('\n'.encode())[-7].split(':'.encode())[-1].decode('utf-8').strip().capitalize()
            responses.append(response)
            print('Response : {}'.format(response))
            program_time = time.time() - start_time
            times.append(program_time)
            count += 1
            if count == 501:
                break
        return(queries, responses, times)


query_list, response_list, time_list = evaluate()
print(query_list, response_list, time_list)
df =  pd.DataFrame({'Query' : query_list, 'Response' : response_list, 'Time' : time_list})
df.to_csv('Blender_90M_bot_response.csv', index=True)

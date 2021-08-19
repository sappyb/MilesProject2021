import sys
from checkkeyword import checkkeywords 

from sentiment_score import sentiment_scores 

state = sys.argv[-1].split(':')[1]
flags_for_message = sys.argv[-1].split(':')[2]
sys.argv[-1] = sys.argv[-1].split(':')[0]
list_of_word = [ i.strip('?').strip(' ').strip('!').strip('.').strip(',').lower() for i in sys.argv[1:] ]

full_sentence = ' '.join(sys.argv[1:])




'''

send the list of word to check for key word

'''
results = checkkeywords(list_of_word, state, flags_for_message)
'''

send the full_sentence for sentiment score

'''

scores = sentiment_scores(full_sentence)


output = '{}:{}'.format(results, scores)
print(output)

import writer

def did_i_get_lana_pregnant():
    f=open('text/text.txt','r')
    answer_to_my_question=f.readlines()
    return answer_to_my_question

my_question=did_i_get_lana_pregnant()

for checking_my_answer in my_question:
    print(checking_my_answer)
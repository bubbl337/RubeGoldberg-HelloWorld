import writer


def getHelloWorld():
    f = open("./text.txt", "r")
    output = f.readlines()
    return output


my_question = getHelloWorld()

for checking_my_answer in my_question:
    print(checking_my_answer)
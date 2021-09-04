a = 0
with open('file_task_2.txt') as file_:
    print('Number of lines: ', len(file_.readlines()))
    file_.seek(0)
    list_ = file_.readlines()
    for i in range(len(list_)):
        a += list_[i].count(' ')
        number_words = len(list_) + a
    print('number of words: ', number_words)
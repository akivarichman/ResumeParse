import re


class Resumes:
    def __init__(self, name):
        self.name = name
        self.mwl = []
        self.boolean_list = []
        self.score = 0


def check(key_word, master_word_list):
    for i in range(len(master_word_list)):
        if key_word.lower() == master_word_list[i].lower():
            return True
    return False


def main():
    resume_list = ['resume1.txt', 'resume2.txt']
    key_words = ['hi']
    rlist = []

    for resume in resume_list:
        print(resume)
        filename = resume
        obj = Resumes(filename)
        file = open(filename,'r')
        # master_word_list = []
        # score = 0
        line = file.readline()
        while line:
            words = re.split('[^a-zA-Z0-9]', line)
            words = ' '.join(words).split()
            for i in range(len(words)):
                obj.mwl.append(words[i])
            line = file.readline()
        file.close()

        key_words = input("Enter your key words: ")
        
        keyword_list = re.split('[^a-zA-Z0-9]', key_words)
        # boolean_list = []

        for i in range(len(keyword_list)):
            is_there = check(keyword_list[i], obj.mwl)
            obj.boolean_list.append(is_there)
            if is_there:
                obj.score += 1
            print(keyword_list[i], " ", is_there)
        print(obj.score)

        rlist.append(obj)

        results = zip(keyword_list, obj.boolean_list)
    
    for obj in rlist:
        print(obj.name)
        print(obj.mwl)
        print(obj.boolean_list)
        print(obj.score)


if __name__ == "__main__": # to ensure that importing of this module into another program will not automatically run it
    main()
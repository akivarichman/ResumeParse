import re


def check(key_word, master_word_list):
    for i in range(len(master_word_list)):
        if key_word.lower() == master_word_list[i].lower():
            return True
    return False


def main():
    master_word_list = []
    score = 0
    file = open('/Users/akivarichman/Desktop/Headstarter/Projects/ResumeParse/ResumeParse/resume.txt', 'r')
    
    line = file.readline()
    while line:
        words = re.split('[^a-zA-Z0-9]', line)
        words = ' '.join(words).split()
        for i in range(len(words)):
            master_word_list.append(words[i])
        line = file.readline()
    file.close()

    key_words = input("Enter your key words: ")

    keyword_list = re.split('[^a-zA-Z0-9]', key_words)
    
    for i in range(len(keyword_list)):
        is_there = check(keyword_list[i], master_word_list)
        if is_there:
            score += 1
        print(keyword_list[i], " ", is_there)
    print(score)


if __name__ == "__main__": # to ensure that importing of this module into another program will not automatically run it
    main()
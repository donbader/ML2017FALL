""" Q1 of hw0: word counts """
#!/usr/bin/env python3
# -*- coding=utf-8 -*-


def main():
    """ main """
    input_file = open("words.txt", 'r')
    output_file = open("Q1.txt", 'w')

    for line in input_file:
        idx = 0
        word_list = line.strip().split(' ')
        word_dict = dict((word, word_list.count(word)) for word in word_list)
        for key, count in word_dict.items():
            output_file.write("%s %s %s\n" % (key, idx, count))
            idx += 1

    # delete last character '\n'
    output_file.seek(output_file.tell() - 1)
    output_file.truncate()

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()

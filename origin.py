#! /usr/bin/env python3

import re

#file: origin.txt

#find all occurances of heritable, inherit, inheritance, and other forms 
#of these words using a regular expression. including caps

#format: {line number it was found on} SPACE(\t) {word} NEWLINE(\n) 

#put meaningful units of code into functions
#make script importable using "if __name__ == '__main__':" flow control
#write informative docstrings to document script and functions
#Try to keep code flexible/dynamic so it can be used for other files




def get_wordform():
        """Finds the words 'heritable' 'inherit', 'inheritance' and 
        other forms of the words and puts them into a new file including 
        the line that the word was found on and a tab inbetween. This is 
        done using regular expression. Each occurance needs to be on a new 
        line. 
        """


        output_file = "origin_list.txt"

        with open('origin.txt', 'r') as f_in, open(output_file,"w") as f_out:
            for line_num, line in enumerate(f_in, start=1):
                words = line.split()
                for word in words:
                    if "herit" in word.lower():
                        f_out.write(f"{line_num}\t{word}\n")



if __name__ == '__main__':
    print(get_wordform())



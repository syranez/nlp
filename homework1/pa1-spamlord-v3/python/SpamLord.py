import sys
import os
import re
import pprint

mail_regex = [
    '((?:\w+\.)*\w+)[ ]?@[ ]?((?:\w+\.)*\w+)\.(\w{2,10})',
    '(\w+)&#x40;([\w+\.]*\w+)\.(\w{2,10})',
    'mailto:(\w+)%20at%20(\w+)%20dot%20(\w{2,10})',
    ' (\w+) at ([\w+\.]*\w+)\.(\w{2,10})<br>',
    '(\w+) at ([\w+;]*\w+);(\w{2,10})',
    '(\w+) \(followed by &ldquo;@([\w+\.]*\w+)\.(\w{2,10})',
    '([\w+\.]*\w+) \(followed by "@([\w+\.]*\w+)\.(\w+)',
    # engler
    '<address>(\w+) WHERE (\w+) DOM (\w+)</address>',
    # hager
    '(\w+) at((?: \w+ do?t)* \w+ do?t)+ (\w+)'
#              '(\w+) at ([\w+\ ]*\w+) (\w+)',
              ]

# Anderer aufbau: (Host / TLD / name)
mail_regex_2 = ['obfuscate\(\'([\w+\.]*\w+)\.(\w+)\',\'(\w+)\'\);']

mail_regex_3 = [
    # dlwh
    '^([A-Za-z\-]+)@-([A-Za-z\-]+)\.-([A-Za-z\-]+)'
]
# convert spaces to dots
mail_regex_4 = [
    # pal
    'email: (\w+) at ((?:\w+ )*\w+) (edu)'
]

""" 
TODO
This function takes in a filename along with the file object (actually
a StringIO object at submission time) and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers

NOTE: ***don't change this interface***, as it will be called directly by
the submit script

NOTE: You shouldn't need to worry about this, but just so you know, the
'f' parameter below will be of type StringIO at submission time. So, make
sure you check the StringIO interface if you do anything really tricky,
though StringIO should support most everything.
"""
def process_file(name, f):

    res = mail(name, f)
    return res

def mail(name, f):

    res = []
    matches = []

    for line in f:
        for regex in mail_regex:
            matches = (re.findall(regex, line))
            for m in matches:
                print "hager: " + m[0] + "-" + m[1] + "-" + m[2]
                email = '%s@%s.%s' % m
                email = email.replace(";", ".")
                email = email.replace(" dot ", ".")
                email = email.replace(" dot", ".")
                email = email.replace("dot ", ".")
                email = email.replace(" dt ", ".")
                email = email.replace(" dt", ".")
                email = email.replace("dt ", ".")
                email = email.replace(" ", "")
                email = email.replace("..", ".")
                res.append((name,'e',email))

        for regex in mail_regex_2:
            matches = (re.findall(regex,line))
            for m in matches:
                email = m[2] + "@" + m[0] + "." + m[1]
                res.append((name,'e',email))

        for regex in mail_regex_3:
            matches = (re.findall(regex,line))
            for m in matches:
                email = '%s@%s.%s' % m
                email = email.replace("-", "")
                res.append((name,'e',email))

        for regex in mail_regex_4:
            matches = (re.findall(regex,line))
            for m in matches:
                email = '%s@%s.%s' % m
                email = email.replace(" ", ".")
                res.append((name,'e',email))
    return res


"""
You should not need to edit this function, nor should you alter
its interface as it will be called directly by the submit script
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print 'True Positives (%d): ' % len(tp)
    pp.pprint(tp)
    print 'False Positives (%d): ' % len(fp)
    pp.pprint(fp)
    print 'False Negatives (%d): ' % len(fn)
    pp.pprint(fn)
    print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn))

"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""
def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tSpamLord.py <data_dir> <gold_file>'
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])

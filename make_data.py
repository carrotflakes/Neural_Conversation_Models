import csv
import sys
import nlutil
import re


def normalize(sentence):
    sentence = nlutil.decouple_reply(sentence)[1]
    sentence = nlutil.decouple_end_hush(sentence)[0]
    sentence = nlutil.replace_url(sentence, ' ')
    sentence = nlutil.normalize(sentence)
    sentence = re.sub(r'\s+', '', sentence)
    return sentence


if __name__ == '__main__':
    filepath = sys.argv[1]

    src = csv.reader(open(filepath))

    train = csv.writer(open('train.tsv', 'w'), delimiter='\t')
    valid = csv.writer(open('valid.tsv', 'w'), delimiter='\t')
    test = csv.writer(open('test.tsv', 'w'), delimiter='\t')

    for i, row in enumerate(src):
        row = (normalize(row[0]), normalize(row[1]))
        if i % 20 == 0:
            valid.writerow(row)
        elif i % 20 == 1:
            test.writerow(row)
        else:
            train.writerow(row)

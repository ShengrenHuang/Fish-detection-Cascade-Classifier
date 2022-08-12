import os

def generate_negative_description_file():
    with open('neg.txt','w') as f:
        for filename in os.listdir('negative'):
            f.write('negative/'+filename+'\n')


def generate_positive_description_file():
    with open('pos.txt','w') as f:
        for filename in os.listdir('positive'):
            f.write('positive/'+filename+' 1 0 0 590 445'+'\n')
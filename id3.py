# coding=utf-8
# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés A01063685
# Raúl Mar A00512318
# Artificial Intelligence
# Assignment: Decision Trees
# Implementation of ID3 based on a dataset
# -----------------------------------------------------------------------------

import fileinput
import sys
import math
from collections import OrderedDict
# from collections import OrderedDict


def splitData(data, attributes, idx):
    values = {k:[] for k in attributes}
    for d in data:    
        values[d[idx]].append(d)
    return values

def getFrequency(data, labels):
    values = {k:[] for k in labels}
    for d in data: 
        values[d[-1]].append(d)
    return values

def entropy(values, total):
    ent = 0.0
    for _, v in values.items():
        if len(v) != 0:
            ent += (-(len(v)/total) * math.log(len(v)/total, 2.0))
    return ent


def information_gain(total_entropy, values, labels):
    i_g = 0.0
    total = 0.0
    #Gain(S, A) = Entropy(S) - ∑( ( |Sv|/|S| ) x Entropy(Sv) )
    for _, v in values.items():
        if v:
            total += len(v)
    for k, v in values.items():
        if v:
            val = getFrequency(v, labels)
            # print('?')
            i_g += (len(v)/total) * entropy(val, len(v))
    return total_entropy - i_g


# Clean initial string to get only the necessary info
def input_reading():
    # Variables to save the according data
    data_relation = ''
    attributes_data = OrderedDict()
    attribute_list = []
    data = []
    start_reading = False
    lines = []

    for line in fileinput.input():
        lines.append(line)

    for line in lines:
        # check if line is not a comment
        if line[0] is not '%':
            #remove spaces
            line = line.strip()
            if len(line):
                if start_reading:
                    line = line.split(',')
                    data.append(line)
                elif line.startswith('@relation'):
                    line = line.split()
                    data_relation = line[1]
                elif line.startswith('@attribute'):
                    line = line[11:]
                    line = line.replace('{', "")
                    line = line.replace('}', "")
                    line = line.replace(',', "")
                    line = line.split()
                    attribute = line[0]
                    attributes_data[attribute] = line[1:]
                    attribute_list.append(attribute)
                elif line.startswith('@data'):
                    start_reading = True    
    return (attributes_data, data_relation, attribute_list, data)


def id3(data, attributes, attributes_list, attr, tabs, indx, labels):
    tabs += 1
    # splitted_values = splitData(data, attributes[attr], indx)
    freq_data = getFrequency(data, labels)
    e = entropy(freq_data, len(data))
    if e == 0.0:
        space = " "
        if not data:
            # print(data)
            print("".join([space for _ in range(tabs*2)]) + "ANSWER: ")
            return
        else:
            print("".join([space for _ in range(tabs*2)]) + "ANSWER: " + data[0][-1])
            return
    # get information gain for each of the attributes_list
    new_entropies = {}
    for i, k in enumerate(attributes_list[:-1]):
        if k:
            attr_splitted = splitData(data, attributes[k], i)
            new_entropies[k] = information_gain(e, attr_splitted, attributes[attributes_list[-1]])
    # if attr == 'having_IP_Address':
    #     print(new_entropies)
    #     return
    best_attr = max(new_entropies, key=new_entropies.get)
    new_split_values = splitData(data, attributes[best_attr], attributes_list.index(best_attr))

    for k, v in new_split_values.items():
        getFrequency(v, labels)

    indx = attributes_list.index(best_attr)

    for k, v in new_split_values.items():
        if v:
            if k == 'having_IP_Address':
                # print('values->')
                # for i in v:
                #     print(i)
                # print('best_attr->', best_attr, '\n')
                return
                # id3(v, attributes, attributes_list, best_attr, tabs, indx)
            print(''.join([' ' for _ in range(tabs*2)]) + best_attr + ': ' + k)
            id3(v, attributes, attributes_list, best_attr, tabs, indx, labels)

        
# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    attributes, _, attributes_list, data = input_reading()
    # print(data)
    # print(sys.version)
    # i = attributes_list.index('result')
    # s = set()
    # for d in data:
    #     # print(d[i])
    #     s.add(d[i])
    # print(s)
    labels = attributes[attributes_list[-1]]
    # print(labels)
    # print(attributes_list)
    # print(attributes[label])
    id3(data, attributes, attributes_list, attributes_list[-1], -1, len(attributes_list) - 1, labels)

if __name__ == '__main__':
    main()

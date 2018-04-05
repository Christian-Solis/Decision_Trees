# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés A01063685
# Raúl Mar A00512318
# Artificial Intelligence
# Assignment: Decision Trees
# Implementation of ID3 based on a dataset
# -----------------------------------------------------------------------------

import fileinput
import math


def splitData(data, attributes, idx):
    values = {k:[] for k in attributes}
    # print('attributes split data->',attributes)
    for d in data:
        # print(d, idx)
        values[d[idx]].append(d)
    # print("splitData->", values)
    # for k, v in values.items():
    #     print(k, v)
    #     print()
    return values

def getFrequency(data, labels):
    values = {k:[] for k in labels}
    for d in data: 
        values[d[-1]].append(d)
    # print('freq ->', values)
    # for k, v in values.items():
    #     print(k, v)
    #     print()
    return values

def entropy(values, total):
    ent = 0.0
    # print(values)
    # print()
    for _, v in values.items():
        if len(v) != 0:
            # return 0.0
            ent += (-(len(v)/total) * math.log(len(v)/total, 2.0))
    return ent


def information_gain(total_entropy, values, labels):
    # print('t_e->', total_entropy)
    i_g = 0.0
    total = 0.0
    #Gain(S, A) = Entropy(S) - ∑( ( |Sv|/|S| ) x Entropy(Sv) )
    for _, v in values.items():
        # print(v)
        if v:
            total += len(v)
    # print('total len', total)
    # print("i_gain->")
    # for k, v in values.items():
    #     print(k, v)
    #     print()
    for k, v in values.items():
        if v:
            # print("information_gain=>", k)
            val = getFrequency(v, labels)
            # print('val', val)
            # print('e=?', entropy(val, len(v)))
            # print('lenv=?, ', len(v))
            i_g += (len(v)/total) * entropy(val, len(v))
    # print('i_g fi->', i_g)
    return total_entropy - i_g

# def best_attribute():


# Clean initial string to get only the necessary info
def input_reading():
    # Variables to save the according data
    data_relation = ''
    attributes_data = {}
    attribute_list = []
    data = []
    start_reading = False

    lines = []
    for line in fileinput.input():
        lines.append(line)

    print(lines)

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


def id3(data, attributes, attributes_list, attr, tabs, indx):
    tabs += 1
    # splitted_values = splitData(data, attributes[attr], indx)
    freq_data = getFrequency(data, attributes[attributes_list[-1]])
    e = entropy(freq_data, len(data))
    # print('entropy->', e)
    if e == 0.0:
        print(''.join([' ' for _ in range(tabs * 2)]) + 'ANSWER: ' + data[0][-1])
        return
    # # get information gain for each of the attributes_list
    new_entropies = {}
    # print()
    # print("aqui el pedo")
    for i, k in enumerate(attributes_list[:-1]):
        # print("empueza")
        if k:
            # print(i, k)
            attr_splitted = splitData(data, attributes[k], i)
            new_entropies[k] = information_gain(e, attr_splitted, attributes[attributes_list[-1]])
    # print(new_entropies)

    best_attr = max(new_entropies, key=new_entropies.get)
    # print("best atr->", best_attr)
    # # print()
    new_split_values = splitData(data, attributes[best_attr], attributes_list.index(best_attr))
    for k, v in new_split_values.items():
        getFrequency(v, attributes[attributes_list[-1]])
    # for a in new_split_values:
    #     print(a)
    # attributes.pop(best_attr, None)
    # print("attrbts=>", attributes)
    # print("attrs_list=>", attributes_list)
    indx = attributes_list.index(best_attr)
    # attributes_list = [a for a in attributes_list if a != best_attr]
    # attributes_list[indx] = ''
    for k, v in new_split_values.items():
        # print("k new split->", k)
        print(''.join([' ' for _ in range(tabs * 2)]) + best_attr + ': ' + k)
        # print(k, v)
        # print("v->", v, "attributes->", attributes, "attributes_list->", attributes_list, "best_attr", best_attr, "tabs->", tabs)
        # print()
        id3(v, attributes, attributes_list, best_attr, tabs, indx)

        
# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    # test = open('ID3.in','r')
    attributes, _, attributes_list, data = input_reading()
    print(attributes)
    print(attributes_list)
    print(data)
    # getFrequency(data, attributes[attributes_list[-1]])
    # d = splitData(data, attributes[attributes_list[3]], 3)
    # for k, v in d.items():
    #     print()
    #     getFrequency(v, attributes[attributes_list[-1]])
    # print("EMPEZAR")
    id3(data, attributes, attributes_list, attributes_list[-1], -1, len(attributes_list) - 1)
    # print(getFrequency(data, attributes[attributes_list[-1]]))
    # splitted_values = getFrequency(attributes[attributes_list[-1]], data, len(attributes_list) - 1)
    # total_entropy = entropy(values, len(data))
    # entropies = {}
    # for idx, val in enumerate(attributes_list[:-1]):
    #     print(idx, val)
        # values = getFrequency(attributes[val], data, idx)
        # print(values)
        # entropies[val] = information_gain(total_entropy, values, attributes[attributes_list[-1]])
        
    # print(entropies)
    # tag = max(entropies, key=entropies.get)
    # print(tag)
    # new_attr_list = [x for x in attributes_list[:-1] if x != tag]
    # print(new_attr_list)
    # values = getFrequency(attributes[tag], data, attributes_list.index(tag))
    # print("\nNEW VALUES")
    # # print(values)
    # for k, v in values.items():
    #     print(k, v)
    # root = Node(tag, False, attributes[tag])
    # print(root.children)


if __name__ == '__main__':
    main()

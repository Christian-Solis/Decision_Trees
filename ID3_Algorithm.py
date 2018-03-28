# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés A01063685
# Raúl Mar A00512318
# Artificial Intelligence
# Assignment: Decision Trees
# Implementation of ID3 based on a dataset
# -----------------------------------------------------------------------------

import sys

# Clean initial string to get only the necessary info
def input_reading(initial_input):

    # Variables to save the according data
    attributes_data = {}
    list_of_attributes = []
    data_relation = ''
    data_content = []

    # Strip the input to remove whitespace
    for single_line in initial_input:
        # Strip lines with no %
        if single_line[0] is not '%':
            single_line = single_line.strip()
            # Replace or split according to start of line
            # if start of line is @attribute
            if single_line.startswith('@attribute'):
                # Ignore characters of @attribute word
                single_line = single_line[11:]
                # Replace unwanted chars
                single_line = single_line.replace('{',"")
                single_line = single_line.replace(',',"")
                single_line = single_line.replace('}',"")
                single_line = single_line.split()
                # Separate attribute and data
                att = single_line[0]
                attributes_data[att] = single_line[1:]
                # Save list of attributes
                list_of_attributes.append(att)
            # If start of line is @relation
            elif single_line.startswith('@relation'):
                single_line = single_line.split()
                # Save the data relation
                data_relation = single_line[1]
            # If start of line is not @attribute or @relation
            else:
                # Separate data by comma and save in list
                single_line = single_line.split(',')
                data_content = single_line[1]

        return(attributes_data, list_of_attributes, data_relation, data_content)
# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    test = open('ID3.in','r')
    input_reading(test)

if __name__ == '__main__':
    main()

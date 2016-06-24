#Program make two random lists and serch common elements
import random

def common_elements_finding(first_list, second_list):
    c = [i for i in first_list if i in second_list]
    return c

def common_elements_in_lists():
    first_list, second_list  = [], []
    
    while len(first_list) < 10 and len(second_list) < 11:
        first_list.append(random.randint(1, 10))
        second_list.append(random.randint(1, 10))
    print first_list,second_list

    common_array = common_elements_finding(first_list, second_list)

    return common_array

if __name__ == '__main__':
    print common_elements_in_lists()
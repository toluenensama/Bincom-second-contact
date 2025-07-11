import os
import re
from typing import List

def getcwd():
    current_directory = os.getcwd()
    return current_directory


def read_full_name(filename="myName.txt"):
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as f:
            name = f.read()
        
        names = name.split(" ")
        first_name = names[0]
        middle_name = names[1]
        last_name = names[2] 
    return f"First name: {first_name} \n Middle name: {middle_name} \n Last name: {last_name}"


def read_and_find_file(filename="baby2008.html"):
    matchesline: List = []
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as f :
            for line in f:
               match = re.findall(r"<td>(.*?)</td>",line)
               name = [item for item in match if item != []]
               data = [item for item in name if not item.isdigit()]
               matchesline.append((data))
    return [" ".join(item) for item in matchesline if item != []]



# print(read_and_find_file())

def binary_search(arr:List,target:str):
    begining,end = 0, len(arr)-1
    while begining <= end:
        middle = (begining + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            begining = middle + 1
        else:
            end = middle - 1
    
    return -1


def search_results(arr,name):
    index = binary_search(arr,name)
    if index > -1:
        return f"The name {name} was found at index {index}"
    else:
        return f"The name {name} was not found"

names: List[str] = read_and_find_file()
names.sort()


print(getcwd())

print(binary_search(names,'Reagan Avah'))
print(read_full_name())
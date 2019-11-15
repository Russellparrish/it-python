import os
from banner import banner
banner("HTML TAG COUNTER", "BY RUSSELL")
print("welcome to the HTML counter")

def get_full_path(name):
    filename = name
    return filename

def load(filename):
    data = []
    filename = get_full_path(f"{filename}")
    print(f'..........loading from {filename}')
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def count_tag(file):
    text =str(file)
    tag_count = 0
    previous_char = None
    for char in text:
        if char != '/' and previous_char == '<':
            tag_count += 1
        previous_char = char
    return tag_count
while True:
    filename = input("please enter your html: ")
    html = load(filename)
    num_tags = count_tag(html)
    print(f'the file {filename} contains {num_tags} tags')
    if input("would you like to count another html(Y/N)") == "Y":
        True
    else:
        break

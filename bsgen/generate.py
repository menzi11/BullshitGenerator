import os
import random, json
import sys

import inquirer

xx = "Test"
repeatetime = 1

# read files
data_file_dict = dict()
for path, subdirs, files in os.walk('bsgen/data'):
    for file in files:
        with open(os.path.join(path, file), "r", encoding="utf8") as f:
            bullshitf = json.load(f)
            data_file_dict[bullshitf['name']] = os.path.join(path, file)


def card_shuffle(slist):
    global repeatetime
    pool = list(slist) * repeatetime
    while True:
        random.shuffle(pool)
        for element in pool:
            yield element


def new_paragraph():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

def main():
    source_select = [
        inquirer.List('source',
                      message="select source data",
                      choices=data_file_dict.keys(),
                      )
    ]
    source = inquirer.prompt(source_select)['source']

    with open(data_file_dict[source], "r", encoding="utf8") as f:
        bullshitf = json.load(f)

    data = bullshitf['data']
    rules = bullshitf['rules']

    xx = input("Input article theme:")
    for x in xx:
        tmp = str()
        while (len(tmp) < 1000):
            branch = random.randint(0, 100)
            if branch < 5:
                tmp += new_paragraph()
            else:
                for i in rules:
                    for j in i:
                        tmp_data = random.choice(data[j])
                        for k in list(data.keys()):
                            if k in tmp_data:
                                tmp_data = tmp_data.replace(k, random.choice(data[k]))
                        tmp += tmp_data

        tmp = tmp.replace("x", xx)
        print(tmp)


if __name__ == "__main__":
    main()

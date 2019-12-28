import os

import yaml


def get_data():
    with open("./Data/"+os.sep+"mss.yaml",'r',encoding="utf-8")as f:
        data =  yaml.safe_load(f)
        lis = []
        for i in data.values():
            lis.append(tuple(i.values()))

    return lis


# print(get_data())
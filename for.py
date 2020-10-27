import  yaml

with open("./data.yml") as f:
    res = yaml.safe_load(f)
    data1 = res["name"]["value"][0]
    print(data1)

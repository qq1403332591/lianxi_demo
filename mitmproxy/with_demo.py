import yaml


def test_case():
    with open('./quote.json',encoding='utf-8') as f:
        data = yaml.load(f)
        new_data = data['data']['items'][0]['quote']['name']
        print(new_data)


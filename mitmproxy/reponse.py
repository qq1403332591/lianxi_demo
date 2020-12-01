import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 过滤url
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 将response转化成Python对象
        data = json.loads(flow.response.content)
        # 将response中的name 修改成xxx
        data['data']['items'][0]['quote']['name'] = "hog"
        # 将修改完的数据 赋值给response原始数据,赋值回去这里用到.text
        flow.response.text = json.dumps(data)


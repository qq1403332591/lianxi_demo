from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "batch" in flow.request.pretty_url and "quote.json" in flow.request.pretty_url:
        with open("D:\LB_HogwartsTest\mitmproxy\quote.json",encoding='utf-8') as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),
                {"Content-Type": "application/json"}
            )
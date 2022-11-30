# coding=utf-8
from head import head, pp, pg
from base import getFullRule
from flask import Flask, request, abort, render_template
from requests import get
from urllib.parse import urlencode
from gevent import pywsgi


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sub")
def sub():
    # return "Hello World!"
    url = request.args
    if "interval" in url:
        interval = url["interval"]
    else:
        interval = "600"
    url = url.get("url")
    status_code = get(url).status_code
    if 200 != status_code:
        pass
        # abort(status_code)
        # return
    urltem = {
            "target": "clash",
            "url": "https://sub.xeton.dev/sub?target=clash&url="+url+"&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini",
            }
    url = "https://proxy-provider-converter.geniucker.top"\
          "/api/convert?" + urlencode(urltem)
    result = head\
        + pp.format(url, interval, url, interval, url, interval, url, interval, url, interval)\
        + pg + "rules:\n" + getFullRule()
    return result, {'Content-Type': 'text/yaml;charset=utf-8'}


@app.route("/test")
def test():
    import urllib.request
    url = request.args
    url = url.get("url")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}
    Request = urllib.request.Request(url)
    r = urllib.request.urlopen(Request).read()
    return r.decode('utf-8')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=221, debug=True)
    # server = pywsgi.WSGIServer(('0.0.0.0', 221), app)
    # server.serve_forever()

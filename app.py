import json

from flask import Flask, request

import Ashare


app = Flask(__name__)


@app.route('/request', methods=["GET"])
def request_info():
    code = request.args.get("code")
    df = Ashare.get_price(code=code, count=365)
    data = {"now_price": str(df.close[-1]),
            "MA_180": str(MyTT.MA(df.close.values, 180)[-1]),
            "MA_100": str(MyTT.MA(df.close.values, 100)[-1]),
            "MA_30": str(MyTT.MA(df.close.values, 30)[-1]),
            "MA_7": str(MyTT.MA(df.close.values, 7)[-1])}
    return json.dumps(data)


if __name__ == '__main__':
    app.run()

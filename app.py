import json

import pandas as pd
from flask import Flask, request

import Ashare
import MyTT

app = Flask(__name__)

code_name = pd.read_csv('code_name.csv')


@app.route('/request', methods=["GET"])
def request_info():
    code = request.args.get("code")
    df = Ashare.get_price(code=code, count=365)
    data = {"now_price": str(df.close[-1]),
            "name": request_code_name(code),
            "MA_180": str(MyTT.MA(df.close.values, 180)[-1]),
            "MA_100": str(MyTT.MA(df.close.values, 100)[-1]),
            "MA_30": str(MyTT.MA(df.close.values, 30)[-1]),
            "MA_7": str(MyTT.MA(df.close.values, 7)[-1])}
    return json.dumps(data)


def request_code_name(code):
    try:
        return code_name[code_name['code'] == int(code[-6:])]['name'].values[0]

    except:
        return "股票" + code


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=2345,
        debug=False
    )

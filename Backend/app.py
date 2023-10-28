import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


def load_csv_to_df(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)



@app.route('/test', methods=['GET'])
def get_test():
    return '<p>Hello World</p>'


@app.route('/user_info', methods=['GET'])
def get_basic_user_info():
    username = request.args.get('username')
    password = request.args.get('password') # ideally this would be encrypted and stored differently

    

    pass




if __name__ == '__main__':
    app.run()


import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


def load_file_to_df(file_path: str) -> pd.DataFrame:
    if file_path[:-4] == '.csv':
        return pd.read_csv(file_path)
    else:
        raise 

@app.route('/test', methods=['GET'])
def get_test():
    return '<p>Hello World</p>'


if __name__ == '__main__':
    app.run()
import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify, request, make_response
from datetime import datetime, timedelta

class DataFiles():
    ''' All the files that contains data. '''
    DIRECTORY = r'./Backend/Data'
    USERS = fr'{DIRECTORY}/Users.csv'
    TRANSACTIONS = fr'{DIRECTORY}/Transactions.csv'
    MONTHLY_BUDGET = fr'{DIRECTORY}/MonthlyBudget.csv'
    INCOME = fr'{DIRECTORY}/Income.csv'
    ENVELOPES = fr'{DIRECTORY}/Envelopes.csv'
    END_OF_MONTH_ASSETS = fr'{DIRECTORY}/EndOfMonthAssets.csv'

def get_data(file: str, identifier: int = -1) -> pd.DataFrame:
    ''' Retrieves data for a corresponding file, filtered by an identifier. '''
    df = pd.read_csv(file)

    if identifier > 0:
        df = df.loc[df['ID'] == identifier]
    
    return df


def get_next_id(file: str) -> int:
    '''Retrieves the successor ID from a specified data file.'''
    prevIds: pd.DataFrame = get_data(file)['ID']
    if prevIds.size == 0:
        return 1
    
    return prevIds.max() + 1


def get_user_id(userName: str) -> int:
    df = get_data(DataFiles.USERS)

    df = df.loc[df['UserName'] == userName]
    if df.size < 1:
        return -1
    return df.iloc[0]['UserID']


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/test', methods=['GET'])
def get_test():
    return '<p>Hello World</p>'

@app.route('/new', methods=['POST'])
def new_user():
    '''
    Expecting the following data structure:
    {
        "UserName": string,
        "FirstName": string,
        "LastName": string,
        "InitAssets": float,
    }
    '''
    userName = request.args.get('UserName')
    firstName = request.args.get('FirstName')
    lastName = request.args.get('LastName')
    initAssets = request.args.get('InitAssets')

    if not userName or not firstName or not lastName or not initAssets:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: UserName, FirstName, LastName, and InitAssets.',
                'severity': 'danger'
            }),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    tempDate = datetime.now().replace(day=1) - timedelta(days=1) # move back one month, date is irrelevant
    lastMonth = tempDate.month
    year = tempDate.year

    newUserId = get_next_id(DataFiles.USERS)
    newEomId = get_next_id(DataFiles.END_OF_MONTH_ASSETS)
    
    userInsertStr = f'\n{newUserId},{userName},{firstName},{lastName}'
    endOfMonthInsertStr = f'\n{newEomId},{newUserId},{year},{lastMonth},{initAssets}'

    with open(DataFiles.USERS, 'a') as file:
        file.write(userInsertStr)
    
    with open(DataFiles.END_OF_MONTH_ASSETS, 'a') as file:
        file.write(endOfMonthInsertStr)

    return 'Success', 200


@app.route('/latest_assets', methods=['GET'])
def get_user_assets():
    '''Expect {"UserName": str} as parameters.'''
    userName = request.args.get('UserName')
    if not userName:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: UserName.',
                'severity': 'danger'
            }),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    data: pd.DataFrame = get_data(DataFiles.END_OF_MONTH_ASSETS)
    asset = data.loc[data['UserID'] == get_user_id(userName)].sort_values('Month', ascending=False).iloc[0]['Assets']

    return jsonify({
        'User': userName,
        'Assets': asset
    }), 200




if __name__ == '__main__':
    app.run()


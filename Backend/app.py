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
    return df.iloc[0]['ID']


def append_to_file(file: str, data: str):
    with open(file, 'a') as f:
        f.write(data)


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/test', methods=['GET'])
def get_test():
    return '<p>Hello World</p>'



@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: username, password.',
                'severity': 'danger'
            }),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response


    userId = get_user_id(username)
    if userId < 0:
        return jsonify({'success': False}), 200
    
    user = get_data(DataFiles.USERS, userId)
    actualPassword = user['Password'].iloc[0]

    if password == actualPassword:
        return jsonify({'success': True}), 200
    return jsonify({'success': False}), 200


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
    userName = request.args.get('username')
    password = request.args.get('password')
    firstName = request.args.get('first_name')
    lastName = request.args.get('last_name')
    initAssets = request.args.get('init_assets')

    if not userName or not password or not firstName or not lastName or not initAssets:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: username, password, first_name, last_name, and init_assets.',
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
    
    userInsertStr = f'\n{newUserId},{userName},{password},{firstName},{lastName}'
    endOfMonthInsertStr = f'\n{newEomId},{newUserId},{year},{lastMonth},{initAssets}'

    append_to_file(DataFiles.USERS, userInsertStr)
    append_to_file(DataFiles.END_OF_MONTH_ASSETS, endOfMonthInsertStr)
    
    return 'Success', 200


@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')

    if not username:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: username.',
                'severity': 'danger'
            }),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    userId = get_user_id(username)
    tempDate = datetime.now().replace(day=1) - timedelta(days=1) # move back one month, date is irrelevant
    lastMonth = tempDate.month
    lastMonthsYear = tempDate.year
    year = datetime.now().year
    month = datetime.now().month

    # get assets
    allAssets = get_data(DataFiles.END_OF_MONTH_ASSETS)
    assets = allAssets.loc[
        (allAssets['UserID'] == userId) &
        (allAssets['Year'] == lastMonthsYear) &
        (allAssets['Month'] == lastMonth)
    ]['Assets'].iloc[0]
    del allAssets
    
    # get monthly budget
    allBudgets = get_data(DataFiles.MONTHLY_BUDGET)
    budget = allBudgets.loc[
        (allBudgets['UserID'] == userId) &
        (allBudgets['Year'] == year) &
        (allBudgets['Month'] == month)
    ]['Amount'].iloc[0]
    del allBudgets

    # get envelopes 
    allEnvelopes = get_data(DataFiles.ENVELOPES)
    allEnvelopes = allEnvelopes.loc[
        (allEnvelopes['UserID'] == userId) & 
        (allEnvelopes['Year'] == year) &
        (allEnvelopes['Month'] == month)
    ]
    envelopes = []
    for index, row in allEnvelopes.iterrows():
        envelopes.append({
            'id': int(row['ID']),
            'name': row['Name'],
            'amount': float(row['Budget'])
        })
    del allEnvelopes

    # get transactions
    allTransactions = get_data(DataFiles.TRANSACTIONS)
    allTransactions['DatetimeObj'] = pd.to_datetime(allTransactions['Datetime'])
    allTransactions['Month'] = allTransactions['DatetimeObj'].dt.month
    allTransactions['Year'] = allTransactions['DatetimeObj'].dt.year
    allTransactions = allTransactions.loc[
        (allTransactions['Year'] == year) &
        (allTransactions['Month'] == month)
    ]
    transactions = []
    for index, row in allTransactions.iterrows():
        transactions.append({
            'id': int(row['ID']),
            'envelope_id': int(row['EnvelopeID']),
            'datetime': row['Datetime'],
            'name': row['Name'],
            'amount': float(row['Amount'])
        })
    del allTransactions

    # get income
    allIncome = get_data(DataFiles.INCOME)
    allIncome = allIncome.loc[allIncome['UserID'] == userId]
    allIncome['DatetimeObj'] = pd.to_datetime(allIncome['Datetime'])
    allIncome['Month'] = allIncome['DatetimeObj'].dt.month
    allIncome['Year'] = allIncome['DatetimeObj'].dt.year
    allIncome = allIncome.loc[
        (allIncome['Year'] == year) &
        (allIncome['Month'] == month)
    ]
    income = []
    for index, row in allIncome.iterrows():
        income.append({
            'id': int(row['ID']),
            'datetime': row['Datetime'],
            'amount': float(row['Amount'])
            
        })
    
    return jsonify({
        'user': username,
        'assets': float(assets),
        'monthly_budget': float(budget),
        'year': int(year),
        'month': int(month),
        'envelopes': envelopes,
        'transactions': transactions,
        'income': income
    }), 200


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


@app.route('/envelope', methods=['POST'])
def create_envelope():
    '''Creates or updates an envelope depending on if envelope exists already.'''
    username = request.args.get('username')
    name = request.args.get('name')
    budget = request.args.get('budget')

    if not username or not name or not budget:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: username, year, month.',
                'severity': 'danger'
            }),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    userId = get_user_id(username)
    newId = get_next_id(DataFiles.ENVELOPES)
    month = datetime.now().month
    year = datetime.now().year

    toStr = f'\n{newId},{userId},{year},{month},{name},{budget}'
    
    append_to_file(DataFiles.ENVELOPES, toStr)
    
    return 'Success', 200


@app.route('/envelope', methods=['DELETE'])
def delete_envelope():
    username = request.args.get('username')
    name = request.args.get('name')
    month = request.args.get('month')
    year = request.args.get('year')
    budget = request.args.get('budget')

    if not username or not name or not month or not year or not budget:
        response =  make_response(
            jsonify({
                'message': 'Expected parameters: username, year, month, name, budget.',
                'severity': 'danger'
            }),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    userId = get_user_id(username)

    envelopes: pd.DataFrame = get_data(DataFiles.ENVELOPES)
    envelopes.drop(envelopes.loc[
        (envelopes['UserID'] == userId) &
        (envelopes['Year'] == year) &
        (envelopes['Month'] == month) &
        (envelopes['Name'] == name) &
        (envelopes['Budget'] == budget)
    ], inplace=True)

    envelopes.to_csv(DataFiles.ENVELOPES, index=False)

    return 'Success', 200


#@app.route('/envelope', methods=['PUT'])
#def update_envelope():



if __name__ == '__main__':
    app.run()


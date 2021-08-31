from flask import Flask, jsonify,request
import numpy as np
import pandas as pd
import sys
# import simplejson
from sklearn.impute import SimpleImputer
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.get_json(force=True)
     query_df = pd.DataFrame(json_)
     query_dp = query_df.copy(deep=True)
     query_dp['x12'] = query_dp['x12'].str.replace('$','')
     query_dp['x12'] = query_dp['x12'].str.replace(',','')
     query_dp['x12'] = query_dp['x12'].str.replace(')','')
     query_dp['x12'] = query_dp['x12'].str.replace('(','-')
     query_dp['x12'] = query_dp['x12'].astype(float)
     query_dp['x63'] = query_dp['x63'].str.replace('%','')
     query_dp['x63'] = query_dp['x63'].astype(float)
     
    #  prediction = lr.predict(query)
     return ({'results':list(query_dp['x76'])})
if __name__ == '__main__':
    app.run(port=3133,debug=True)
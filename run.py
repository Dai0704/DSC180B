import sys
import json
import pandas as pd


sys.path.insert(0, 'src')

from eda import data,eda,describe
from model import plot_TPR_FPR,plot_TPR_FDR,plot_rates,prediction_model



def main(targets):

    testin_config = json.load(open("config/testin-params.json"))
    testout_config = json.load(open("config/testout-params.json"))
    data_config = json.load(open("config/data-params.json"))
    eda_config = json.load(open("config/eda-params.json"))
    model_config = json.load(open("config/model-params.json"))

    if 'data' in targets:

        df = data(**data_config)

    if 'eda' in targets:

        df = data(**data_config)

        eda(df, **eda_config)
        describe(df, **eda_config)
        
    if 'model' in targets:

        df = data(**data_config)
        
        prediction_model(df, **model_config)

        
    if 'test' in targets:
        
        df = data(**testin_config)

        eda(df, **testout_config)
        describe(df, **testout_config)
        prediction_model(df, **testout_config)
        


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
import json
import _pickle as pkl
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bedrooms,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bedrooms
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    global __data_columns
    global __locations
    
    with open("/Users/gideonogunbanjo/Documents/TrendTroves/Server/artifcats/columns.json", "r") as f: 
        data_columns = json.load(f)['data_columns']
        __data_columns = data_columns[3:] 
        __locations = __data_columns 
        
    global __model
    if __model is None:
        with open('/Users/gideonogunbanjo/Documents/TrendTroves/Server/artifcats/model.pkl', 'rb') as f: 
            __model = pkl.load(f)
    print("Loading saved artifacts...done")


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2)) 

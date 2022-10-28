import pickle
import json
import numpy as np
import pandas as pd
import config

class BengaluruHouse():
    def __init__(self,size,bath,balcony,area_type,new_total_sqft):
        self.size = size
        self.bath = bath
        self.balcony = balcony
        self.area_type = "area_type_" + area_type
        self.new_total_sqft = new_total_sqft

    def load_file(self):

        with open(config.PICKLE_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_predicted_h_price(self):
        self.load_file()

        area_type_index = self.json_data["columns"].index(self.area_type)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.json_data["size_dict"][self.size]
        array[1] = self.bath
        array[2] = self.balcony
        array[3] = self.new_total_sqft
        array[area_type_index] = 1

        print("Array-->",array)
        predicted_price = self.model.predict([array])[0]
        return np.around(predicted_price,2)

if __name__ == "__main__":
    size='19 BHK'
    bath=40.0
    balcony=80.0
    area_type ='Built-up  Area'
    new_total_sqft=12000.0

    bhp = BengaluruHouse(size,bath,balcony,area_type,new_total_sqft)
    price = bhp.get_predicted_h_price()
    print(f"predicted bengalaru house price is {price} lac")

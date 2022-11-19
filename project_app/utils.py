import numpy as np
import config
import pickle
import json

class Iris():
    def __init__(self,Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.Id= Id
        self.SepalLengthCm =SepalLengthCm
        self.SepalWidthCm  =SepalWidthCm
        self.PetalLengthCm =PetalLengthCm
        self.PetalWidthCmp =PetalWidthCm

    def load_model(self):
        with open(config.MODEL_FILE,"rb") as f:
            self.model=pickle.load(f)
        with open(config.JSON_FILE,"r") as f:
            self.json_data=json.load(f)
    def get_species(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["Column_names"]))
        
        test_array[0] = self.Id
        test_array[1] = self.SepalLengthCm
        test_array[2] = self.SepalWidthCm
        test_array[3] = self.PetalLengthCm
        test_array[4] = self.PetalWidthCmp

        print("test_array:",test_array)
        predict_species = np.around(self.model.predict([test_array])[0],2)
        return predict_species
        # return self.json_data["Species"][str(predict_species)]

# if __name__=="__main__":
#     Id =1.0
#     SepalLengthCm =6
#     SepalWidthCm  =4
#     PetalLengthCm =1.5
#     PetalWidthCm  =0.3

#     spes = Iris(Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
#     spes.get_species()

        

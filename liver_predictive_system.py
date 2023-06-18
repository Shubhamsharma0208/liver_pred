import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
#load saved model
load_model=pickle.load(open('C:/Users/Shubham/Desktop/Machine learning/liver_prediction/Trained_model.pkl','rb'))



input = (17,1,0.9,0.3,202,22,19,7.4,4.1,1.2)

#changing input to numpy array
data=np.asarray(input)
# reshaping of data
reshape_data=data.reshape(1,-1)
# normalise data
mms=MinMaxScaler()
nor_data=mms.fit_transform(reshape_data)
print(nor_data)
#prediction using mmodel
prediction=load_model.predict(nor_data)
print(prediction)

if (prediction==0):
    print("You are healthy")
else:
    print("you have liver disease ")
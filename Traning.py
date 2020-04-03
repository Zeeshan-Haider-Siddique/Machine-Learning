import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def Data_split (Data ,Ratio):
    np.random.seed(42)
    shuffeld = np.random.permutation(len(Data))
    test_size = int(len(Data)*Ratio)
    test_induce = shuffeld[ : test_size]
    train_induce = shuffeld[test_size : ]
    return df.iloc[test_induce],df.iloc[train_induce]

if __name__ == "__main__":
    df = pd.read_csv('G:\\Smart Xeshi\\CronaVirus\\Data.csv')
    train,test= Data_split(df , 0.2)

    X_train = train[['Fever','BodyPain','Age','RunyNose','DifficultyBreath']]
    X_test = test [['Fever','BodyPain','Age','RunyNose','DifficultyBreath']]
    Y_train = train[ ['InfactionProb'] ]
    Y_test = test[ ['InfactionProb'] ]

    LR =LogisticRegression(random_state=0)
    LR.fit(X_train,Y_train)

    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(LR, file)
    file.close()

    

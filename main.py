from flask import Flask , render_template , request
app = Flask(__name__)
import pickle


file = open('model.pkl', 'rb')
LR=pickle.load(file)
file.close()

@app.route('/' , methods =["GET" , "POST"])
def hello_world():
    if request.method == "POST":
        myDict =request.form
        Fever = int(myDict['Fever'])
        BodyPain = int(myDict['BodyPain'])
        Age = int(myDict['Age'])
        RunnyNose = int(myDict['RunnyNose'])
        DifficultyBreath = int(myDict['DifficultyBreath'])

        InputFeatures = [Fever,BodyPain,Age,RunnyNose,DifficultyBreath]
        InFactionProbabolity= LR.predict_proba([InputFeatures])[0][1]
        print(InFactionProbabolity)
        return render_template('show.html' , inf =round(InFactionProbabolity * 100 ))
    return render_template('index.html')
    
    #return'Hello, World!' +str(InFactionProbabolity)

if __name__ == "__main__":
    app.run(debug=True)
    

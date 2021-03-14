from flask import Flask, redirect, url_for, render_template, request
import pickle
import numpy as np


app = Flask(__name__, template_folder='.')

# ML model path
model_path = "ML_model/model.pkl"
classifier = pickle.load(open(model_path, 'rb'))

@app.route("/", methods=["POST", "GET"])
def home():
        return render_template("home.html")

@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            acousticness = request.form['acousticness']
            danceability = request.form['danceability']
            energy = request.form['energy']
            instrumentalness = request.form['instrumentalness']
            liveness = request.form['liveness']
            loudness = request.form['loudness']
            speechiness = request.form['speechiness']
            tempo = request.form['tempo']
            valence = request.form['valence']
            popularity = request.form['popularity']
            duration_ms = request.form['duration_ms']
            year = request.form['year']
            features = [acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence, popularity, duration_ms, year]
            if not None in features:
                new_record = np.array([[acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence, popularity, duration_ms, year]])
                predict_result = classifier.predict(new_record)
                return redirect(url_for('predict', prediction=predict_result))
            else:
                return redirect(url_for('home'))
        except:
                return redirect(url_for('home'))

    else:
        return render_template("index.html")
    

@app.route("/predict/<prediction>")
def predict(prediction):
    return render_template("predict.html", prediction=prediction)
    

if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=8501, debug=True)
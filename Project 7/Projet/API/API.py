from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import mlflow

app = Flask(__name__)

# Charger le modèle enregistré avec MLflow
model = mlflow.lightgbm.load_model("model")

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        best_tresh = 0.53

        file = request.files['file']

        if file:
            # Lire le fichier CSV
            df = pd.read_csv(file)
            df_id = df["SK_ID_CURR"]

            df.drop(columns=["SK_ID_CURR"], inplace=True)

            # Faire des prédictions avec le modèle
            predictions = model.predict_proba(df)[:, 1]
            results = np.where(predictions >= best_tresh, "Refusé", "Accepté")

            # Ajouter les prédictions au DataFrame
            results = pd.DataFrame(results, index=df.index, columns=["Results"])
            results["NB"] = df.index
            results["ID"] = df_id
            results["Predict"] = np.round(predictions * 100, 2)
            results = results[["NB", "ID", "Predict", "Results"]]

            # Convertir le DataFrame en HTML pour l'affichage
            result_html = results.to_html(classes='table table-striped', index=False)

            return render_template('results.html', tables=[result_html])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__) #crear aplicación

# Cargar el modelo
with open('../../Datos_Mod3/Pickels/mejor_modelo.pkl', 'rb') as f:
    model = pickle.load(f)

# Cargar los transformers
with open('../../Datos_Mod3/Pickels/transformer_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('../../Datos_Mod3/Pickels/transformer_one.pkl', 'rb') as f:
    one = pickle.load(f)

with open('../../Datos_Mod3/Pickels/transformer_target.pkl', 'rb') as f:
    target = pickle.load(f)

variables_one = ['Education',
 'Gender',
 'JobLevel',
 'JobRole',
 'StockOptionLevel',
 'TrainingTimesLastYear',
 'JobInvolvement',
 'PerformanceRating']

@app.route("/") # decorador
def home(): # principal, funcion
    return jsonify({'mensaje': 'API de predicción en funcionamiento',
                   'endpoints': {'/predict': 'Usa este endpoint para realizar predicciones'}}) # siempre poner return

# @app.route("/predict", methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()  # Obtener datos       
#         df_pred = pd.DataFrame(data, index=[0])
#         print(df_pred)

#         # Procesamiento
#         tasa_de_cambio = 0.0113
#         df_pred['MonthlyIncome'] = df_pred['MonthlyIncome'].apply(lambda x: x * tasa_de_cambio)

#         df_pred['Attrition'] = df_pred['Attrition'].map({'Yes': 1, 'No': 0})        
#         df_pred['Education'] = df_pred['Education'].astype('category')
#         df_pred['JobLevel'] = df_pred['JobLevel'].astype('category')
#         df_pred['StockOptionLevel'] = df_pred['StockOptionLevel'].astype('category')
#         df_pred['EnvironmentSatisfaction'] = df_pred['EnvironmentSatisfaction'].astype(str)
#         df_pred['JobSatisfaction'] = df_pred['JobSatisfaction'].astype(str)
#         df_pred['WorkLifeBalance'] = df_pred['WorkLifeBalance'].astype(str)
#         df_pred['JobInvolvement'] = df_pred['JobInvolvement'].astype('category')
#         df_pred['PerformanceRating'] = df_pred['PerformanceRating'].astype('category')
#         df_pred['TrainingTimesLastYear'] = df_pred['TrainingTimesLastYear'].astype('category')
#         df_pred.drop(columns=['Over18', 'EmployeeCount', 'StandardHours', 'EmployeeID'], inplace=True)
        
#         print(df_pred.columns)

#         col_numericas = df_pred.select_dtypes(include=np.number).columns
#         print(col_numericas)
#         df_pred[col_numericas] = scaler.transform(df_pred[col_numericas])

#         df_one = pd.DataFrame(one.transform(df_pred[variables_one]).toarray(), columns=one.get_feature_names_out())
#         df_pred = pd.concat([df_pred, df_one], axis=1)
#         df_pred.drop(columns=variables_one, inplace=True)

#         df_pred = target.transform(df_pred)

#         prediccion = model.predict(df_pred)
#         probabilidad = model.predict_proba(df_pred)
#         return jsonify({'prediccion': prediccion.tolist()[0],
#                         'probabilidad': probabilidad.tolist()[0][1]})

#     except KeyError as e:
#         return jsonify({'error': f'Falta una columna clave: {str(e)}'})
#     except ValueError as e:
#         return jsonify({'error': f'Error en los valores de las columnas: {str(e)}'})
#     except Exception as e:
#         return jsonify({'error': f'Error inesperado: {str(e)}'})


# @app.route("/predict", methods = ['POST']) # decorador
# def predict(): # principal, funcion
#     try:
#         data = request.get_json() # coge el json al usuario que nos da la info
#         df_pred = pd.DataFrame(data, index=[0])
#         print(df_pred)

#         tasa_de_cambio = 0.0113
#         df_pred['MonthlyIncome'] = df_pred['MonthlyIncome'].apply(lambda x: x * tasa_de_cambio)

#         df_pred['Attrition'] = df_pred['Attrition'].map({'Yes': 1, 'No': 0})        
#         df_pred['Education'] = df_pred['Education'].astype('category')
#         df_pred['JobLevel'] = df_pred['JobLevel'].astype('category')
#         df_pred['StockOptionLevel'] = df_pred['StockOptionLevel'].astype('category')
#         df_pred['EnvironmentSatisfaction'] = df_pred['EnvironmentSatisfaction'].astype(str)
#         df_pred['JobSatisfaction'] = df_pred['JobSatisfaction'].astype(str)
#         df_pred['WorkLifeBalance'] = df_pred['WorkLifeBalance'].astype(str)
#         df_pred['JobInvolvement'] = df_pred['JobInvolvement'].astype('category')
#         df_pred['PerformanceRating'] = df_pred['PerformanceRating'].astype('category')
#         df_pred['TrainingTimesLastYear'] = df_pred['TrainingTimesLastYear'].astype('category')
#         # df_pred.drop(columns=['Over18', 'EmployeeCount', 'StandardHours', 'EmployeeID'], inplace=True)
        
#         print(df_pred.columns)

#         col_numericas = df_pred.select_dtypes(include=np.number).columns
#         print(col_numericas)
#         df_pred[col_numericas] = scaler.transform(df_pred[col_numericas])

#         df_one = pd.DataFrame(one.transform(df_pred[variables_one]).toarray(), columns= one.get_feature_names_out()) #metodo para ponerle nombre
#         df_pred = pd.concat([df_pred, df_one], axis=1)
#         df_pred.drop(columns = variables_one, axis=1, inplace=True)

#         df_pred = target.transform(df_pred)

#         prediccion = model.predict(df_pred)
#         probabilidad = model.predict_proba(df_pred)
#         return jsonify({'prediccion': prediccion.tolist()[0],
#                         'probabilidad': probabilidad.tolist()[0][1]})

#     except:
#         return jsonify({'respuestas':'Ha habido un problema en el envío de datos'})
    
@app.route("/predict", methods=['POST'])
def predict():
    # try:
    # Obtener datos JSON y convertir a DataFrame
    data = request.get_json()
    df_pred = pd.DataFrame(data, index=[0])
    print("Datos iniciales recibidos:")
    print(df_pred)

    # Procesar datos
    tasa_de_cambio = 0.0113
    df_pred['MonthlyIncome'] = df_pred['MonthlyIncome'].apply(lambda x: x * tasa_de_cambio)

    # Mapear y convertir tipos
    df_pred['Education'] = df_pred['Education'].astype('category')
    df_pred['JobLevel'] = df_pred['JobLevel'].astype('category')
    df_pred['StockOptionLevel'] = df_pred['StockOptionLevel'].astype('category')
    df_pred['EnvironmentSatisfaction'] = df_pred['EnvironmentSatisfaction'].astype(str)
    df_pred['JobSatisfaction'] = df_pred['JobSatisfaction'].astype(str)
    df_pred['WorkLifeBalance'] = df_pred['WorkLifeBalance'].astype(str)
    df_pred['JobInvolvement'] = df_pred['JobInvolvement'].astype('category')
    df_pred['PerformanceRating'] = df_pred['PerformanceRating'].astype('category')
    df_pred['TrainingTimesLastYear'] = df_pred['TrainingTimesLastYear'].astype('category')

    # Escalado de columnas numéricas
    col_numericas = df_pred.select_dtypes(include=np.number).columns
    print("Columnas numéricas:", col_numericas)
    df_pred[col_numericas] = scaler.transform(df_pred[col_numericas])

    # One-Hot Encoding
    print("Aplicando One-Hot Encoding...")
    df_one = pd.DataFrame(one.transform(df_pred[variables_one]).toarray(), columns=one.get_feature_names_out())
    df_pred = pd.concat([df_pred, df_one], axis=1)
    df_pred.drop(columns=variables_one, inplace=True)

    # Añadir columna ficticia para Target Encoding
    df_pred['Attrition'] = np.nan
    df_pred = target.transform(df_pred)
    df_pred.drop(columns=['Attrition'], inplace=True)

    # Alinear columnas con las esperadas por el modelo
    expected_columns = model.feature_names_in_
    df_pred = df_pred.reindex(columns=expected_columns, fill_value=0)

    # Realizar predicción
    prediccion = model.predict(df_pred)
    probabilidad = model.predict_proba(df_pred)

    return jsonify({
        'prediccion': int(prediccion[0]),
        'probabilidad de que se vaya': float(probabilidad[0][1])
    })

if __name__ == '__main__':
    app.run(debug=True)


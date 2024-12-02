import streamlit as st
import pandas as pd
import pickle
import numpy as np
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="💻Predicción de la probabilidad de partida de un empleado",
    page_icon="📠",
    layout="centered",
)

# Título y descripción
st.title(" Predicción de la probabilidad de partida de un empleado")
st.write("Usa esta aplicación para predecir si tus empleados son propensos a irse en el próximo años")

# Mostrar una imagen
# st.image(
#     "C:\Users\DELL\Git\Proyecto8---Predicci-n-de-Retenci-n-de-Empleados\imagen.webp",  # URL de la imagen
#     caption="Retención de tus empleados.",
#     use_column_width=True,
# )


# Cargar los modelos y transformadores entrenados
def load_models():
# Cargar el modelo
    with open('../../Datos_Mod3/Pickels/mejor_modelo.pkl', 'rb') as f:
        model = pickle.load(f)

    # Cargar los transformers
    with open('../../Datos_Mod3/Pickels/transformer_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    with open('../../Datos_Mod3/Pickels/transformer_one.pkl', 'rb') as f:
        target = pickle.load(f)

    with open('../../Datos_Mod3/Pickels/transformer_target.pkl', 'rb') as f:
        one_hot = pickle.load(f)
    return one_hot, target, scaler, model

one_hot,target_encoder, scaler, model = load_models()

st.header("Datos y características del empleado 🧔")
col1, col2 ,col3= st.columns(3)

with col1:
    Age = st.number_input("Edad", min_value=18,max_value=60 , value=30, step=1, help="Elige la edad del trabajador entre 18 y 60")
    Education = st.selectbox("Educación", [1,2,3,4,5], help="Elige la educación del trabajador")
    EducationField= st.selectbox("Campo de Estudio", ['Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree', 'Human Resources'])
    Gender= st.selectbox("Género", ['Female', 'Male'])
    MaritalStatus = st.selectbox("Estado civil", ['Married', 'Single', 'Divorced'], help="Elige el estado civil del empleado")
    NumCompaniesWorked = st.selectbox('Número de compañías', [0,1,2,3,4,5,6,7,8,9], help="Elige el numero de compañías donde el empleado ha trabajado")
    TotalWorkingYears= st.selectbox('Años trabajados',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                       21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])

with col2:
    JobLevel = st.selectbox("Nivel del puesto", [1,2,3,4,5],help="Elige el nivel del puesto del empleado")
    JobRole = st.selectbox('Rol', ['Healthcare Representative', 'Research Scientist','Sales Executive', 'Human Resources', 'Research Director','Laboratory Technician', 'Manufacturing Director','Sales Representative', 'Manager'], help='Elije el rol del empleado')
    BusinessTravel = st.selectbox('Frecuencia de viaje', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'], help='Elige la frecuencia de viaje del trabajador') #min,max,predeterminado
    Department = st.selectbox("Departamento", ['Sales', 'Research & Development', 'Human Resources'], help="Elige el departamento del trabajador")
    DistanceFromHome = st.slider("Distancia de casa al trabajo", 1,30,15 , help="Eligela distancia a casa del trabajador")
    MonthlyIncome= st.slider("Salario mensual",114,2260,500)
    PercentSalaryHike= st.slider('Porcentaje de subida de salario', 11,25,15)
    StockOptionLevel= st.selectbox('Nivel de reparto de acciones', [0,1,2,3])
    YearsWithCurrManager= st.slider("Tiempo bajo su gerente", 1,17,5 , help="Elige el tiempo que lleva trabajando con su mismo gerente")

    
with col3:
    TrainingTimesLastYear= st.number_input('Número de formaciones en el último año', min_value=0,max_value=6 , value=1, step=1)
    YearsAtCompany= st.slider('Años en la compañía actual', 0,40,15)
    YearsSinceLastPromotion= st.number_input('Años desde la última promoción', min_value=0,max_value=15 , value=1, step=1)
    EnvironmentSatisfaction= st.selectbox('Nivel de satisfacción con el entorno', [1,2,3,4])
    JobSatisfaction= st.selectbox('Nivel de satisfacción en el trabajo', [1,2,3,4])
    WorkLifeBalance= st.selectbox('Nivel de satisfacción con el balance vida-trabajo', [1,2,3,4])
    JobInvolvement= st.selectbox('Nivel de implicación en el trabajo', [1,2,3,4])
    PerformanceRating= st.selectbox('Nivel de desempeño laboral del empleado', [1,2,3,4])


# Botón para realizar la predicción
if st.button("Predecir si el empleado se va 🤞"):
    # Crear DataFrame con los datos ingresados    #Comprobar que sean las mismas que la mía y el mismo orden
    new_employee = pd.DataFrame({
        'Age': [Age],
        'BusinessTravel': [str(BusinessTravel)],
        'Department': [str(Department)],
        'DistanceFromHome': [DistanceFromHome],
        'Education': [str(Education)],
        'EducationField' : [str(EducationField)],
        'Gender' : [str(Gender)],
        'JobLevel': [JobLevel],
        'JobRole': [str(JobRole)],
        'MaritalStatus': [str(MaritalStatus)],
        'MonthlyIncome': [MonthlyIncome],
        'NumCompaniesWorked': [NumCompaniesWorked],
        'PercentSalaryHike': [PercentSalaryHike],
        'StockOptionLevel': [str(StockOptionLevel)],
        'TotalWorkingYears': [TotalWorkingYears],
        'TrainingTimesLastYear': [str(TrainingTimesLastYear)],
        'YearsAtCompany': [YearsAtCompany],
        'YearsSinceLastPromotion': [YearsSinceLastPromotion],
        'YearsWithCurrManager': [YearsWithCurrManager],
        'EnvironmentSatisfaction' : [str(EnvironmentSatisfaction)],
        'JobSatisfaction' : [str(JobSatisfaction)],
        'WorkLifeBalance': [str(WorkLifeBalance)],
        'JobInvolvement': [str(JobInvolvement)],
        'PerformanceRating': [str(PerformanceRating)]      
    })
  
    new_employee=pd.DataFrame(new_employee)

    new_employee_encoded = scaler.transform(new_employee)
    new_employee_encoded = pd.DataFrame(new_employee_encoded)
    # new_house_encoded.drop(columns=6,inplace=True)
    # new_employee["Attrition"]=new_employee_encoded[6]

    
    
    col_encode = ["Gender", "PerformanceRating", "Education", "JobLevel", "StockOptionLevel", "JobRole", "TrainingTimesLastYear", "JobInvolvement"]
    onehot = one_hot.transform(new_employee[col_encode])
    # Obtenemos los nombres de las columnas del codificador
    column_names = one_hot.get_feature_names_out(col_encode)
    # Convertimos a un DataFrame
    onehot_df = pd.DataFrame(onehot.toarray(), columns=column_names)
    #onehot_df.drop(columns=col_encode,inplace=True)                    
    
    
             #Añadir el Onehot
    # Codificación de las columnas categóricas
    new_employee.drop(columns = col_encode,inplace=True)
    new_employee_encoded = pd.concat([new_employee, onehot_df], axis=1)

    new_employee_encoded["Attrition"] = np.nan
    new_employee_encoded = target_encoder.transform(new_employee_encoded)
    

    new_employee_encoded2=new_employee_encoded.copy()
    new_employee_encoded3=new_employee_encoded.copy()
 
    # Realizar la predicción
    prediction = model.predict(new_employee_encoded)[0]
    if prediction ==0:
        pred="No se irá de la empresa"
    else:
        pred="Se irá de la empresa"
    # dicc_pred={0:"No se irá de la empresa",
    #            1:"Se irá de la empresa"}
    # prediction_encoded=prediction.map(dicc_pred)
    # y_pred=modelo_final.predict(x)
    # Mostrar el resultado
    st.success(f"El empleado que has consultado {pred}")
    st.balloons()

st.markdown(
    """
    ---
    **Proyecto creado con el potencial de la ciencia de datos.**  
    Desarrollado con ❤️ usando Streamlit.
    """,
    unsafe_allow_html=True,
)
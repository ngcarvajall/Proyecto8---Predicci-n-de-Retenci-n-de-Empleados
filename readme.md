![Oficina](imagen.webp)
# 📊 Predicción de Rotación de Empleados: Modelos de Machine Learning

## 📖 Descripción

Este proyecto aborda un problema crucial para los departamentos de Recursos Humanos: predecir qué empleados tienen mayor probabilidad de dejar la empresa en el próximo año. A partir de datos históricos, hemos desarrollado y evaluado modelos de Machine Learning para identificar patrones y tendencias en la rotación laboral.

---

## 🗂️ Estructura del Proyecto

### **Distribución de Carpetas**
```
├── Datos/                # Datos originales y transformados
│   ├── Datos_Mod1/       # Datos del Modelo 1
│   ├── Datos_Mod2/       # Datos del Modelo 2
│   ├── Datos_Mod3/       # Datos del Modelo 3
├── Modelos/              # Archivos de modelos entrenados y Notebooks de cada modelo
│   ├── Modelo 1/
│   │   ├── 1_EDA.ipynb              # Exploración de datos
│   │   ├── 2_Estandarizar.ipynb     # Escalado y estandarización
│   │   ├── 3_Encoding.ipynb         # Codificación de variables
│   │   ├── 4_Métricas.ipynb         # Evaluación del modelo
│   ├── Modelo 2/
│   │   ├── 1_EDA.ipynb              # Exploración de datos
│   │   ├── 2_OUTLIERS.ipynb         # Tratamiento de outliers
│   │   ├── 3_Estandarizar.ipynb     # Escalado y estandarización
│   │   ├── 4_Métricas.ipynb         # Evaluación del modelo
│   │   ├── 5_Métricas_Dif.ipynb     # Comparativa de métricas usando distintos hiperparámetros
│   ├── Modelo 3/
│   │   ├── 1_EDA.ipynb              # Exploración de datos
│   │   ├── 2_OUTLIERS.ipynb         # Tratamiento de outliers
│   │   ├── 3_Estandarizar.ipynb     # Escalado y estandarización
│   │   ├── 4_Métricas.ipynb         # Evaluación del modelo
│   │   ├── 5_Métricas_copy.ipynb    # Comparativa de métricas
│   │   ├── API.ipynb                # Implementación de la API de predicción
│   │   ├── main.py                  # Script principal para la API
│   │   ├── Streamlit.py             # Interfaz con Streamlit (en prueba)
├── src/                  # Scripts de procesamiento y modelado
├── README1.md             # Descripción del proyecto
```

---

## 🛠️ Instalación y Requisitos

Este proyecto utiliza Python 3.8 y las siguientes bibliotecas:

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [imbalanced-learn](https://imbalanced-learn.org/stable/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [xgboost](https://xgboost.readthedocs.io/)
- [streamlit](https://streamlit.io/)

### Instalación:
1. Clona este repositorio:
   ```bash
   git clone <URL DEL REPOSITORIO>
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Resultados y Conclusiones

Para todos mis modelos utilicé la misma secuencia de pasos de preprocesamiento:
   - **1** Tratamiento de Outliers
   - **2** Estandarización de variables numéricas
   - **3** Encoding de variables categóricas

### Modelo 1:
- **Duplicados:** Se descubrió una gran cantidad de duplicados al eliminar la columna `EmployeeID`, lo que afecta la calidad del modelo.
- **Nulos:** Las variables categóricas fueron completadas con "Desconocido" y las numéricas mediante `IterativeImputer`.
- **Balanceo:** Este modelo no tiene balanceo, por lo que la variable respuesta "Attrition" está desbalanceada.
- **Conclusión:** Las métricas del modelo, especialmente usando XGBoost, son altas, pero reflejan un sobreajuste debido a los duplicados. Este modelo predictivo obtuvo métricas de evaluación bastante buenas, algunas cercanas a 1 (lo óptimo). Sin embargo, identificamos que más del 60% de los datos del conjunto son duplicados. Esto significa que muchos de los datos del conjunto de prueba ya han sido vistos durante el entrenamiento, lo que provoca que las predicciones sean perfectas en esos casos. Como resultado, las métricas obtenidas no reflejan la verdadera capacidad del modelo para generalizar a datos nuevos y pueden estar sobreestimadas debido a esta redundancia en los datos.

### Modelo 2:
- **Reducción de datos:** Sin duplicados, solo queda el 40% de los datos originales.
- **Outliers:** Se eliminaron los outliers (multivariados al 100% usando el LOF) basados en vecinos 15, 25, y 35.
- **Balanceo:** Este modelo tampoco tiene balanceo, lo que afecta las métricas.
- **Conclusión:** Decision Tree tuvo el mejor desempeño, pero las métricas fueron más realistas pero significativamente peores debido al desbalanceo con respecto al Modelo 1, ya que aunque trabajo con los datos correctos aún no he balanceado.

### Modelo 3:
- **Balanceo:** Se usaron técnicas de balanceo como Tomek y SMOTENC para equilibrar la variable respuesta en un 55-45.
- **Resultados:** Este modelo es el más robusto, con métricas más realistas y generalización adecuada.
- **Conclusión:** Las mejores métricas se obtuvieron con XGBoost y Gradient Boosting, sin embargo las métricas más realistas, generalistas y confiables eran dadas por la regresión logística. Por ende me he quedado con este modelo. Debajo dejo un breve resumen de cómo fueron los resultados.

### Comparativa Final:
| **Modelo**          | **Generalización** | **Sobreajuste** | **Métricas en test** | **Velocidad** | **Comentario**                      |
|----------------------|--------------------|-----------------|----------------------|---------------|--------------------------------------|
| **Regresión logística** | Alta               | Bajo            | Buenas (0.87-0.88)  | Muy alta      | Consistente, eficiente, confiable.  |
| **XGBoost**          | Media              | Alto            | Muy buenas (0.91)   | Moderada      | Alto rendimiento pero sobreajusta.  |
| **Random Forest**    | Media              | Alto            | Muy buenas (0.91)   | Baja          | Costoso y sobreajustado.            |
| **Gradient Boosting**| Moderada           | Moderado        | Buenas (0.88-0.90)  | Moderada      | Competitivo, buen equilibrio.       |
| **Decision Tree**    | Baja               | Bajo            | Débiles (0.79)      | Moderada      | Modelo menos competitivo.           |


# 📊 Predicción de Rotación de Empleados: Conclusiones

Este proyecto aborda un problema crucial para los departamentos de Recursos Humanos: predecir qué empleados tienen mayor probabilidad de dejar la empresa en el próximo año. A partir de datos históricos, hemos desarrollado y evaluado modelos de Machine Learning para identificar patrones y tendencias en la rotación laboral. 

El enfoque no solo es técnico, sino también analítico, destacando los siguientes hallazgos clave:

## 📌 Principales Descubrimientos

- **Edad**: 
  - El punto más alto de rotación se encuentra en empleados menores de 30 años. A partir de esa edad, las salidas disminuyen progresivamente.

- **Distancia al trabajo**:
  - Los empleados que viven a menor distancia del lugar de trabajo tienen mayor probabilidad de abandonar la empresa.

- **Salario**:
  - Aquellos con ingresos por debajo de la media son más propensos a salir. Esto se relaciona con la mediana salarial, que se encuentra dentro de este grupo de salidas.

- **Incrementos salariales**:
  - Aunque no se identificaron patrones muy marcados, los empleados con porcentajes de aumento salarial menores son más propensos a abandonar la empresa.

- **Años trabajados**:
  - El primer año es crítico en la rotación laboral. La mayor parte de las salidas ocurre durante el primer año en la empresa, bajo un nuevo manager o tras recibir un ascenso.

- **Frecuencia de viajes**:
  - Los empleados que viajan con poca frecuencia son más propensos a irse.

- **Departamentos**:
  - El departamento de investigación y desarrollo concentra la mayor fuga de empleados.

- **Nivel educativo**:
  - Los empleados con un nivel educativo intermedio (tipo 3) tienen mayor probabilidad de salir. A partir de este nivel, las salidas disminuyen, sugiriendo que empleados con mayor formación prefieren quedarse.

- **Campo de educación**:
  - Los empleados con formación en ciencias de la vida (Life Sciences) y medicina (Medical) presentan mayores índices de rotación. Esto podría estar relacionado con la especialización de la empresa y las proyecciones personales de los empleados.

- **Género**:
  - Los hombres son el grupo con mayor probabilidad de rotación.

- **Nivel de puesto (JobLevel)**:
  - Los empleados en los niveles más bajos tienen mayores índices de rotación, posiblemente asociados con salidas prematuras.

- **Tipo de rol**:
  - Tres roles destacan por su alta rotación: Research Scientist, Sales Executive y Laboratory Technician. Esto refleja tendencias en sectores como ciencias (ya observadas en la categoría de Educación) y ventas, que suelen ser áreas con alta rotación debido a sus exigencias.

- **Estado civil**:
  - Los empleados solteros son el grupo con mayor rotación, probablemente debido a una mayor flexibilidad y menos compromisos personales.

- **Entrenamientos**:
  - Los empleados que recibieron entre 2 y 3 entrenamientos en el último año presentan mayores tasas de salida.

- **Satisfacción del empleado**:
  - No se observaron diferencias significativas entre los niveles de satisfacción.

- **Balance vida-trabajo y desempeño**:
  - Los empleados en el grupo 3 de Balance Vida-Trabajo, Job Involvement y Performance Rating tienen mayor presencia en los casos de rotación.

## 📈 Conclusiones Finales

Estos hallazgos ofrecen una visión integral de los factores más relevantes que influyen en la rotación de empleados. La identificación de estos patrones no solo permite construir modelos predictivos más precisos, sino que también facilita la implementación de estrategias específicas para reducir la rotación laboral y mejorar la retención del talento.

---

## 🔄 Próximos Pasos

- Implementar técnicas adicionales de feature engineering para mejorar la precisión.

---

## ✒️ Autor

- **Nelson Carvajal** - [GitHub](https://github.com/ngcarvajall)

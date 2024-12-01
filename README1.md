
# 📊 Predicción de Rotación de Empleados: Modelos de Machine Learning

## 📖 Descripción

Este proyecto aborda un problema crucial para los departamentos de Recursos Humanos: predecir qué empleados tienen mayor probabilidad de dejar la empresa en el próximo año. A partir de datos históricos, hemos desarrollado y evaluado modelos de Machine Learning para identificar patrones y tendencias en la rotación laboral.

El enfoque no solo es técnico, sino también analítico, explorando preguntas como:
- ¿Es la satisfacción laboral un predictor clave?
- ¿Las largas horas de trabajo o las relaciones tensas con los jefes afectan la decisión de quedarse?
- ¿Qué papel juegan las promociones o aumentos de salario?

Los resultados no solo buscan ser precisos, sino también útiles para tomar decisiones informadas en la gestión del talento.

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
│   │   ├── 5_Métricas_Dif.ipynb     # Comparativa de métricas
│   ├── Modelo 3/
│   │   ├── 1_EDA.ipynb              # Exploración de datos
│   │   ├── 2_OUTLIERS.ipynb         # Tratamiento de outliers
│   │   ├── 3_Estandarizar.ipynb     # Escalado y estandarización
│   │   ├── 4_Métricas.ipynb         # Evaluación del modelo
│   │   ├── 5_Métricas_copy.ipynb    # Comparativa de métricas
│   │   ├── API.ipynb                # Implementación de la API de predicción
│   │   ├── main.py                  # Script principal
│   │   ├── Streamlit.py             # Interfaz con Streamlit
├── src/                  # Scripts de procesamiento y modelado
├── Métricas/             # Reportes de métricas de evaluación
├── README.md             # Descripción del proyecto
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

### Modelo 1:
- **Duplicados:** Se descubrió una gran cantidad de duplicados al eliminar la columna `EmployeeID`, lo que afecta la calidad del modelo.
- **Nulos:** Las variables categóricas fueron completadas con "Desconocido" y las numéricas mediante `IterativeImputer`.
- **Balanceo:** Este modelo no tiene balanceo, por lo que la variable respuesta "Attrition" está desbalanceada.
- **Conclusión:** Las métricas del modelo, especialmente usando XGBoost, son altas, pero reflejan un sobreajuste debido a los duplicados (más del 60% de los datos del test están en el entrenamiento).

### Modelo 2:
- **Reducción de datos:** Sin duplicados, solo queda el 40% de los datos originales.
- **Outliers:** Se eliminaron los outliers al 100% basados en vecinos 15, 25, y 35.
- **Balanceo:** Este modelo tampoco tiene balanceo, lo que afecta las métricas.
- **Conclusión:** Decision Tree tuvo el mejor desempeño, pero las métricas fueron significativamente peores debido al desbalanceo.

### Modelo 3:
- **Balanceo:** Se usaron técnicas de balanceo como Tomek y SMOTENC para equilibrar la variable respuesta en un 55-45.
- **Resultados:** Este modelo es el más robusto, con métricas más realistas y generalización adecuada.
- **Conclusión:** Las mejores métricas se obtuvieron con XGBoost y Gradient Boosting.

### Comparativa Final:
| **Modelo**          | **Generalización** | **Sobreajuste** | **Métricas en test** | **Velocidad** | **Comentario**                      |
|----------------------|--------------------|-----------------|----------------------|---------------|--------------------------------------|
| **Regresión logística** | Alta               | Bajo            | Buenas (0.87-0.88)  | Muy alta      | Consistente, eficiente, confiable.  |
| **XGBoost**          | Media              | Alto            | Muy buenas (0.91)   | Moderada      | Alto rendimiento pero sobreajusta.  |
| **Random Forest**    | Media              | Alto            | Muy buenas (0.91)   | Baja          | Costoso y sobreajustado.            |
| **Gradient Boosting**| Moderada           | Moderado        | Buenas (0.88-0.90)  | Moderada      | Competitivo, buen equilibrio.       |
| **Decision Tree**    | Baja               | Bajo            | Débiles (0.79)      | Moderada      | Modelo menos competitivo.           |

---

## 🔄 Próximos Pasos

- Implementar técnicas adicionales de feature engineering para mejorar la precisión.
- Evaluar otros modelos como LightGBM o CatBoost para comparar rendimiento.
- Automatizar el pipeline de preprocesamiento y entrenamiento.

---

## ✒️ Autor

- **Nelson Carvajal** - [GitHub](https://github.com/ngcarvajall)

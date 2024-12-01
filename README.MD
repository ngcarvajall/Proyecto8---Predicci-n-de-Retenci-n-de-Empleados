Estamos tratando de predecir si un empleado se irá o no en el siguiente año, de acuero a los datos del año pasado.

Modelo 1: 
    - Este modelo no tenía duplicados en uuna primera observación. Sin embargo, al eliminar los ID de los empleados me he dado cuenta que existía una enorme cantidad de duplicados. A pesar de esto, decidí continuar con el proceso del modelo para ver las diferencias entre un modelo entrenado con duplicados y otros que no. 
    - Los nulos que tenía en variables categóricas fueron rellenados con una nueva categoría 'Desconocido', mientras que los nulos de las categorías numéricas los imputé con un Iterative Imputer.
    - De igual forma, este modelo no cuenta con balanceo. Por lo que dentro de mi variable respuesta 'Attrition' existen claras diferencias en proporciones.
    - Este modelo predictivo obtuvo métricas de evaluación bastante buenas, algunas cercanas a 1 (lo óptimo). Sin embargo, identificamos que más del 60% de los datos del conjunto son duplicados. Esto significa que muchos de los datos del conjunto de prueba ya han sido vistos durante el entrenamiento, lo que provoca que las predicciones sean perfectas en esos casos. Como resultado, las métricas obtenidas no reflejan la verdadera capacidad del modelo para generalizar a datos nuevos y pueden estar sobreestimadas debido a esta redundancia en los datos.
    - Para este modelo me quedaría con las métricas del xgboost que son las mejores considerando la circunstancia de un modelo con tantos duplicados.

Modelo 2:
    - Este modelo, al eliminar la columna que identificaba cada usuario de manera individual (EmployeeID) nos deja con menos del 40% de los datos. A partir de este momento, vamos a trabajar con una nueva cantidad de datos para conocerlos y hacer un preprocesamiento para un nuevo modelo.
    - Aquí, al eliminar los nulos nos hemos quedado con una gran cantidad de 'No' en nuestra variable respuesta por encima de su contraparte 'Yes' para la columna Attrition. Esto es un desbalanceo. Para este modelo no vamos a balancear, la intención es ver con este modelo cómo puede predecir con datos desbalanceados y nuestro próximo modelo (Modelo 3) sí tendrá datos balanceados. De esta forma podemos contrastar entre todos.
    - En el primer año de trabajo, hay una gran fuga de empleados.
    - Identifiqué outliers al 60%, me cargué los outliers al 100% tomando en cuenta vecinos del 15,25,35.
    - Para este modelo, donde no hay balanceo, las métricas ya son más realistas. Sin embargo, al tener tanta dominancia de una sola parte de nuestra variable respuesta, vemos como las métricas son muy diferentes al primer modelo. A la vez, estas son mayormente fruto de la aleatoriedad, dígase con bajos valores para el kappa.
    - Para este modelo, me quedo con el decision tree. Para este modelo las métricas brillan por ser bastante malas fruto del enorme desbalanceo.

Modelo 3:
    - Mejor modelo, sin duplicados y balanceado en primer lugar con Tomek para disminuir la el grupo dominante de mi variable respuesta. Esto no provocó una gran caída, sino la desaparición de unos 50 datos. Luego de esto, hice un SmoteNC ya que permite diferenciar las categóricas a la hora de hacer el proceso. Con este hice un balanceo para que mi variable respuesta quede en unos parámetros 55-45. De esta forma no creo tantos valores artificales como para equiparar al 50%.
    - Una vez hecho dicho procedimiento, seguí con mis modelos para ver cuáles métricas eran las mejores y a través de que modelo podía conseguirlas. Debajo dejo un cuadro comparativo respecto a esto.


    | **Modelo**          | **Generalización** | **Sobreajuste** | **Métricas en test** | **Velocidad** | **Comentario**                      |
    |----------------------|--------------------|-----------------|----------------------|---------------|--------------------------------------|
    | **Regresión logística** | Alta               | Bajo            | Buenas (0.87-0.88)  | Muy alta      | Consistente, eficiente, confiable.  |
    | **XGBoost**          | Media              | Alto            | Muy buenas (0.91)   | Moderada      | Alto rendimiento pero sobreajusta.  |
    | **Random Forest**    | Media              | Alto            | Muy buenas (0.91)   | Baja          | Costoso y sobreajustado.            |
    | **Gradient Boosting**| Moderada           | Moderado        | Buenas (0.88-0.90)  | Moderada      | Competitivo, buen equilibrio.       |
    | **Decision Tree**    | Baja               | Bajo            | Débiles (0.79)      | Moderada      | Modelo menos competitivo.           |

Estamos tratando de predecir si un empleado se irá o no en el siguiente año, de acuero a los datos del año pasado.

Modelo 1: 
    - Este modelo no tenía duplicados en uuna primera observación. Sin embargo, al eliminar los ID de los empleados me he dado cuenta que existía una enorme cantidad de duplicados. A pesar de esto, decidí continuar con el proceso del modelo para ver las diferencias entre un modelo entrenado con duplicados y otros que no. 
    - Los nulos que tenía en variables categóricas fueron rellenados con una nueva categoría 'Desconocido', mientras que los nulos de las categorías numéricas los imputé con un Iterative Imputer.
    - De igual forma, este modelo no cuenta con balanceo. Por lo que dentro de mi variable respuesta 'Attrition' existen claras diferencias en proporciones.
    - Este modelo predictivo obtuvo métricas de evaluación bastante buenas, algunas cercanas a 1 (lo óptimo). Sin embargo, identificamos que más del 60% de los datos del conjunto son duplicados. Esto significa que muchos de los datos del conjunto de prueba ya han sido vistos durante el entrenamiento, lo que provoca que las predicciones sean perfectas en esos casos. Como resultado, las métricas obtenidas no reflejan la verdadera capacidad del modelo para generalizar a datos nuevos y pueden estar sobreestimadas debido a esta redundancia en los datos.

Modelo 2:
    - Este modelo, al eliminar la columna que identificaba cada usuario de manera individual (EmployeeID) nos deja con menos del 40% de los datos. A partir de este momento, vamos a trabajar con una nueva cantidad de datos para conocerlos y hacer un preprocesamiento para un nuevo modelo.
    - Aquí, al eliminar los nulos nos hemos quedado con una gran cantidad de 'No' en nuestra variable respuesta por encima de su contraparte 'Yes' para la columna Attrition. Esto es un desbalanceo. Para este modelo no vamos a balancear, la intención es ver con este modelo cómo puede predecir con datos desbalanceados y nuestro próximo modelo (Modelo 3) sí tendrá datos balanceados. De esta forma podemos contrastar entre todos.

Modelo 3:
    - 
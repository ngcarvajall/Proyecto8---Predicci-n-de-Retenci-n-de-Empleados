Estamos tratando de predecir si un empleado se irá o no en el siguiente año, de acuero a los datos del año pasado.

Modelo 1: 
    - Este modelo no tenía duplicados en uuna primera observación. Sin embargo, al eliminar los ID de los empleados me he dado cuenta que existía una enorme cantidad de duplicados. A pesar de esto, decidí continuar con el proceso del modelo para ver las diferencias entre un modelo entrenado con duplicados y otros que no. 
    - Los nulos que tenía en variables categóricas fueron rellenados con una nueva categoría 'Desconocido', mientras que los nulos de las categorías numéricas los imputé con un Iterative Imputer.
    - De igual forma, este modelo no cuenta con balanceo. Por lo que dentro de mi variable respuesta 'Attrition' existen claras diferencias en proporciones.

Modelo 2:

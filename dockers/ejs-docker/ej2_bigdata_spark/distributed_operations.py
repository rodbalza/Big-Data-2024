from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    # Crear configuración y contexto de Spark
    conf = SparkConf().setAppName("DistributedApp")
    sc = SparkContext(conf=conf)

    # RDD con una lista de números del 1 al 10
    data = list(range(1, 11))
    dist_data = sc.parallelize(data, 2)

    # Sumar todos los elementos
    sum_elements = dist_data.reduce(lambda a, b: a + b)
    print(f"Suma de los elementos: {sum_elements}")
    input("Presiona Enter para continuar...")

    # Filtrar los elementos mayores que 5
    greater_than_five = dist_data.filter(lambda x: x > 5).collect()
    print(f"Elementos mayores que 5: {greater_than_five}")
    input("Presiona Enter para continuar...")

    # Contar el número de elementos y calcular el promedio
    count_elements = dist_data.count()
    avg_elements = sum_elements / count_elements
    print(f"Promedio de los elementos: {avg_elements}")
    input("Presiona Enter para continuar...")

    # Agrupar los elementos en pares e impares
    grouped_elements = dist_data.groupBy(lambda x: x % 2 == 0).collect()
    for key, group in grouped_elements:
        print(f"Grupo {key}: {[x for x in group]}")
    input("Presiona Enter para continuar...")

    # Finalizar el contexto de Spark
    sc.stop()

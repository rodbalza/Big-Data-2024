# Usar una imagen oficial de OpenJDK como base, necesario para Spark
FROM openjdk:8-jdk-alpine

# Instalar wget para descargar Spark
RUN apk add --no-cache wget bash

# Descargar Apache Spark (versión 3.5.0)
RUN wget https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz

# Descomprimir Spark
RUN tar -xzf spark-3.5.0-bin-hadoop3.tgz

# Mover Spark al directorio adecuado
RUN mv spark-3.5.0-bin-hadoop3 /usr/local/spark

# Establecer variables de entorno
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Definir el comando para iniciar Spark Shell
CMD ["spark-shell"]



<img style="float: right; margin: 0px 0px 15px 15px;" src="https://wallpaperaccess.com/full/7006038.jpg" width="350px" height="300" />

# Book clasification

+ Ana Rosaura Zamarrón Álvarez - 736222
+ Claudia Celeste Castillejos Jáuregui - 735868

# ProyectoPCD

Este repositorio contiene el proyecto final de la materia de Proyecto de Ciencia de Datos

Este proyecto está dividido en 4 carpetas:
1. app: contiene el archivo main.py donde se contruyó el API, el dockerfile con el que se construyó la imagen, el archivo requirements.txt, y el modelo de sistemas de recomendación.
2. data: contiene los datos con los que se hizo el modelo del sistema de recoemndación.
3. EDA: Contiene un Jupyter notebook donde se hizo la exploración de los datos.

## Introducción
Hoy en día los sistemas de recomendación son parte de la vida cotidiana de gran parte de las personas, lo podemos ver en muchos sitios de internet como las redes sociales, sitios de E-Commerce como Amazon o Mercado Libre, o algúna plataforma de streaming como Netflix o Spotify. Los sistemas de recomendación afectan significativamente en el contenido que consumimos diariamente, por eso es importante que un científico de datos aprenda a utilizaros, tienen un valor significativo para muchas empresas o proyectos.

Para este proyecto se creará un sistema de recomendación donde los productos a recomendar son libros. Es un tema interesante porque dentro del mundo de los sistemas de recomendación los productos a tratar normalmente son películas, productos de una tienda departamental, canciones, etc.; pero no hay muchos ejemplos sobre libros.

El modelo se desplegará en un API donde el usuario podrá hacer la petición para recibir una recomendación de un libro con base en otro que ya leyó. El dataset contiene ratings de 278,858 usuarios que proveen 1,149,780 ratings (explicito / implicito) de alrededor de 271,379 libros.

Los datos se obtuvieron de Kaggle: https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset.

## Antecedentes
Para crear nuestro sistema de recomendación se utilizará un filtrado colaborativo basado en items. Este algoritmo calcula la similitud que hay entre los productos utilizando los ratings que le dieron los usuarios a cada uno y recomienda el producto más similar a los que ya consumió el usuario. Amazon desarrolló el filtrado colaborativo basado en items. En un sistema donde hay más usuarios que elementos, el filtrado basado en items es más rápido y más estable que el basado en usuarios. Es efectivo porque, por lo general, la calificación promedio que recibe un item no cambia tan rápido como la calificación promedio otorgada por un usuario a diferentes items.

## Objetivos
+ Crear un sistema de recomendación de libros utilizando el algoritmo de filtrado colaborativo
+ Hacer un despliegue del modelo utilizando un API.

## Planteamineto del problema
El producto final del proyecto será un programa que sea capaz de recomendar un libro a un usuario. El API que se creará debe ser capaz de recibir información del usuario, puede ser uno o varios libros que le hayan gustado, pero solo pueden ser libros que estén en nuestra base de datos.

# Documentación
Esta es una aplicación Web realizada con el Framework Flask y Bootstrap.
Su próposito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos Postgres utilizando Migraciones.
Las dependencias del proyecto se gestionan con Pipenv.

## Dependencias

Para correr este proyecto se necesita previamente tener instalado Phyton3 y su herramienta Pip.
Para revisar si las tiene instalado, debe ejecutar los siguientes comandos:

```
python -V
pip -V
```

El resultado debiera indicar un número superior a 3 o algo así.
Luego de clonar el repositorio, y para instalar las dependencias debe ejecutar el comando 

`pipenv install`.

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:

Para ejecutar hacia adelante
```
flask db upgrade
```

Para ejecutar hacia atrás
```
flask db downgrade
```

Cuando hacemos algun cambio en un modelo y necesitamos considerar esos cambios también en la base de datos, hay que generar una nueva migración.

```
flask db migrate -m"mensaje de la migración"
```

En caso de modificar un Modelo agregando o modificando un atributo, debemos generar una nueva migración, con el comando:

```
flask db migrate -m "mensaje de la migración"
```

**nota**: Los comandos anteriores se deben ejecutar dentro de `pipenv shell`

## Blueprint

Los blueprint permiten componer aplicaciones desde componentes pequeños. Cada componentes es como una mini aplicación. Permiten crear aplicaciones grandes, pero manteniendo el código y la estructura simples.

## Módulos

Para que los blueprint esten bien organizados, es mejor trabajarlos como módulos, es decir, que estén dentro de una carpeta. Los módulos se pueden anidar, de hecho, nosotros hicimos el módulo `app` con su respectivo `__init__.py` y dentro tenemos otros módulos como el módulo `messages` que es además un blueprint.

## Tarea
Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo a url `/memes` y debe renderiar un html lleno de memes. 


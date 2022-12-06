# FastAPI-Challenge SquadMarker

## Acerca de:

Proporciona una API-Rest pública mediante la cual el usuario puede obtener, listar, editar y eliminar chistes usando como proveedor de datos distintas API.

## Tecnologías:

Lenguaje: Python 3.11.0

Web server: FastAPI

Base Datos: Postgres

ORM: SQLAlchemy

Arquitectura: API-Rest, N-Capas

Documentación: Swagger

Virtualización: Docker

CI/CD: Github Actions

Versión de controles: Git

Repositorio: Github

Test: pytest

## Instalación:


`` python -m pip install -r requirements/dev.txt ``

## Ejecutar test:

`` pytest ``

## Ejecutar proyecto:

`` python -m uvicorn server:app --reload ``

nota: Las variables de entorno se deben configurar como se muestra en el archivo de ejemplo .env.example.

## Base de Datos:

Dada la naturaleza de los datos y su estructura se escogió un modelo de base de datos relacional aplicando postgres como sistema gestor de base de datos.

Fácilmente escalable tanto horizontalmente como vertical, rápida en consultas y altamente compatible con servicios en la nube para su posterior despliegue.

Se adjuntó en el código un archivo con las sentencias para la creación de la base de datos

## Despliegue:

Servicio de backend dockerizado solamente para desarrollo (falto de tiempo para producción). Fácil de integrar con docker-compose, kubernates o servicios de AWS como ECS o EC2.

## Licencia:

Producto de SquadMakers

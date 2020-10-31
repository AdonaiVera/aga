# DS4A project

Present historical information of the development plan of the municipality of Bello - Antioquia to facilitate the vision, and support the management of its administration.

## Installation
Instalar librerías necesarias para el proyecto
```
pip install -r requirements.txt
pip install -r requirements2.txt
```

## Run
Usa este comando para iniciar la app
```bash
streamlit run app.py
```


## Arquitectura 🚀
La arquitectura esta basada en AWS, los servicios utilizados son:
1. EC2 -> En el cual se alojan los algoritmos principales.
2. S3 Bucket -> Se almacena el archivo SIEE subido por las alcaldias.
3. Lambda -> Permite alojar la aplicación que consume la API de Twitter. 
4. RDS -> Se utiliza una base de datos en Postgress. 

_Estas instrucciones te permitirán conocer cuales son los servicios utilizados para lograr desplegar todo el aplicativo._

Mira **Despliegue** para conocer como desplegar el proyecto.
![Alt text](images/Diagrama.png?raw=true "Arquitectura")




### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Da un ejemplo
```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Twitter 🖥
A continuación se algunos ejemplos de twitter en el área de seguridad. 
------
1. RT @EmpresarioVox: El Gobierno oculta que estamos totalmente a la deriva. Hace meses saltó la alarma en la Seguridad Social porque el gasto…
2. RT @laurxweird: "conocí a esta belleza cuando estaba protegiendo a un hombre sin hogar de ser acosado por alguien de seguridad"
Esta es mi…
3. RT @CIDH: Por último, la #CIDH reitera al Estado las recomendaciones formuladas durante su reciente visita in loco, especialmente la de lle…
4. RT @GNB_Sucre: #OperaciónGarraOriental2020 
Nuestros efectivos trabajan de manera articulada con cuerpos policiales para velar por tu segur…
5. RT @Lautafym: La pandemia de las fuerzas de seguridad del mundo tiene mucho más tiempo de vigencia que cualquier otra. Es más difícil de cu…
6. RT @diario24horas: El presidente Andrés Manuel López Obrador elogió el trabajo realizado por titular de la Secretaría de Seguridad y Protec…
7. RT @lqmhr: Tenemos un Canciller que no habla inglés. Es como tener, no sé, una antropóloga como Ministra de Seguridad.
Espero no leer vuestros tweets hablando sobre las medidas de seguridad cuando sois los primeros que no las cumplís máquinas
8. RT @Millerrojas19: @RicardoMolanoV1 @qmoncaleano @MdeFrancisco12 @fdbedout @MeDicenWally Comparto. Totalmente
En Colombia alcanzan un cargo…
9. RT @lvillavicenciom: autoridad civil, es que sus miembros son formados ideológicamente bajo los estertores de la doctrina de la seguridad n…



--------

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️
* **Andres Felipe Velasquez** - *Member DS4a* - [afvrsystems](https://github.com/afvrsystems)
* **Laura Lopez** - *Member DS4a* - [Lauravlopez](https://github.com/Lauravlopez)
* **Natalia Castilla Reyes** - *Member DS4a* - [ancastillar](https://github.com/ancastillar)
* **Olga Angulo** - *Member DS4a* - [Olucya](https://github.com/Olucya)
* **Jhon Rodriguez** - *Member DS4a* - [Lauravlopez](https://github.com/Lauravlopez)
* **Migue Jurado** - *Member DS4a* - [Miguel Jurado](https://github.com/migeruj)
* **Adonai Vera** - *Member DS4a* - [AdonaiVera](https://github.com/AdonaiVera)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/AdonaiVera/Bello/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.


---

# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierías


## Departamento de ciencias computacionales
Computación tolerante a fallas - Sección D06

Profesor: *López Franco Michel Emanuel*

Alumno: *Lomelí Flores Jesús Isaac*

## Istio


### Introducción
<p align="justify"> 
  En la actualidad una de las mejores maneras de realizar sistemas tolerantes a fallos es utilizando las ventajas que da la nube y el uso de microservicios para formar una aplicación nativa en este entorno, permitiendo que cada servicio sea independiente y tenga un mínimo de interconexión con los demás, sin mencionar que se pueden probar algunas versiones de software al levantarlas como servicios independientes. En esta práctica se tratara de replicar lo descrito anteriormente en un entorno local creando dos versiones de un servicio que serán administrados por la malla de servicios istio.
</p>

### ¿Qué es Istio?  

<p align="justify">
Istio es una malla de servicios (es decir, una capa de redes de servicios modernizada) que ofrece una manera transparente e independiente de cualquier lenguaje de automatizar las funciones de red de una aplicación de forma flexible y sencilla. Es una solución muy popular para gestionar los diferentes microservicios que conforman una aplicación nativa de la nube. La malla de servicios de Istio también es compatible con las formas de comunicarse y compartir datos entre ellos que utilizan estos microservicios.

</p>

<p align="justify"> 
Para garantizar la portabilidad en la nube, los desarrolladores deben aprender a crear aplicaciones mediante microservicios con bajo acoplamiento. Al mismo tiempo, los equipos de aplicaciones deben ser capaces de gestionar las aplicaciones nativas de la nube en entornos híbridos y multinube cada vez más grandes. Con Istio, pueden hacerlo.
</p>


### Desarrollo


<p align="justify"> 
Para esta practica se utilizo el codigo de la API de la practica de kubnerntes agregando una segunda version en la que se agrega un nuevo endpoint para poder obtener los libros que tengan una cantidad igual o menos a la ingresada en el paramentro de la ruta. Para esta practica los .yaml de servicio y deploy fueron fusionados y se muestran debajo de estas lineas.
</p>


```.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-kubernetes-jilf-deployment
  labels:
    app: apikubernetes
spec:
  replicas: 3
  selector:
    matchLabels:
      app: apikubernetes
  template:
    metadata:
      labels:
        app: apikubernetes
    spec:
      containers:
      - name: apikubernetes
        image: caasi81/apikubernetes:v1
        ports:
        - containerPort: 8000

---

apiVersion: v1
kind: Service
metadata:
  name: api-kubernetes-jilf-service
  labels:
    app: api-kubernetes-jilf-service
spec:
  selector:
    app: apikubernetes
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  sessionAffinity: None
```


```.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-istio-jilf-deployment
  labels:
    app: apiistio
spec:
  replicas: 3
  selector:
    matchLabels:
      app: apiistio
  template:
    metadata:
      labels:
        app: apiistio
    spec:
      containers:
      - name: apiistio
        image: caasi81/apikubernetes:v2
        ports:
        - containerPort: 8000

---

apiVersion: v1
kind: Service
metadata:
  name: api-istio-jilf-service
  labels:
    app: api-istio-jilf-service
spec:
  selector:
    app: apiistio
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  sessionAffinity: None
```

<p align="justify"> 
Ademas, fue necesaria la creacion de 2 archivos .yaml, uno para el gateway y otro para el virtual service.
</p>


```.yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: api-gateway
spec:
  selector:
    app: istio-ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
```


```.yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: api-service-ingress
spec:
  hosts: 
  - '*'
  gateways:
  - api-gateway
  http:
  - match:
    - uri:
        prefix: /v1/
    rewrite:
        uri: /
    route:
    - destination:
        host: api-kubernetes-jilf-service
        port:
          number: 8000
  - match:
    - uri:
        prefix: /v2/
    rewrite:
        uri: /
    route:
    - destination:
        host: api-istio-jilf-service
        port: 
          number: 8000
```

<p align="justify"> 
Una vez creados los archivos necesarios se procede a descargar e instalar istio, no sin antes agregarlo a las variables del sistema.
</p>

![Instalacion de istio](/Imagenes/Screenshot_63.png)


<p align="justify"> 
Una vez que istio se encuentra instalado se procede a inyectarlo a los contenedores por defecto como se muestra en la imagen siguiente.
</p>

![Inyeccion de istio](/Imagenes/Screenshot_64.png)

<p align="justify"> 
El siguiente paso fue aplicar el gateway y el virtual service. Se comprueba el funcionamiento del gateway de istio.
</p>

![Gateway de istio](/Imagenes/Screenshot_68.png)


<p align="justify"> 
Se procede a agregar kiali y los yaml creados con anterioridad.
</p>

![Se añade kiali](/Imagenes/Screenshot_65.png)

![Aplicacion de yamls service y deploy](/Imagenes/Screenshot_67.png)


<p align="justify"> 
Para mostrar los graficos de kiali es necesario instalar algunas dependencias.
</p>

![Instalacion de dependencias de kiali](/Imagenes/Screenshot_71.png)

<p align="justify"> 
Por ultimo se activa el tunel con minikube.
</p>

![Activacion de tunel](/Imagenes/Screenshot_69.png)

<p align="justify"> 
La siguiente captura es la unica que pudo obtenerse de los graficos en kiali, puesto que por lomitaciones de hardware no fue posible cargar el grafo una vez que los servicios se estaban consumiendo.
</p>

![Graficos de kiali](/Imagenes/Screenshot_70.png)


## Conclusión

<p align="justify"> 
Gracias a esta practica se logro comprender la importancia de los microservicios y la ventaja de utilizar una malla de servicios como istio, puesto que al desarrollar una aplicacion nativa de la nube se manejan microservicios que deberian de funcionar por si solos para que en caso de que alguno falle, el funcionamiento del resto no se vea comprometido o el daño sea menor, asi mismo presenta algunas ventajas para los desarrolladores como es la posibilidad de probar las nuevas versiones de su software en algunos usuarios con ciertas caracteristicas especificadas, o simplemente como balanceo del trafico desviando a uno a los usuario de moviles y a otro los usuario de escritorio.
</p>


## Bibliografía

- ¿Qué es Istio?  |  Google Cloud. (s. f.). Google Cloud. Recuperado el 07 de Mayo de 2023, de https://cloud.google.com/learn/what-is-istio?hl=es

# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierías


## Departamento de ciencias computacionales
Computación tolerante a fallas - Sección D06
Profesor: *López Franco Michel Emanuel*
Alumno: *Lomelí Flores Jesús Isaac*

## Kubernetes


### Introducción


### ¿Qué es Kubernetes?  

<p align="justify">
Kubernetes es una plataforma portable y extensible de código abierto para administrar cargas de trabajo y servicios. Kubernetes facilita la automatización y la configuración declarativa. 
</p>
<p align="justify"> 
Kubernetes ofrece un entorno de administración centrado en contenedores. Orquesta la infraestructura de cómputo, redes y almacenamiento para que las cargas de trabajo de los usuarios no tengan que hacerlo. Esto ofrece la simplicidad de las Plataformas como Servicio (PaaS) con la flexibilidad de la Infraestructura como Servicio (IaaS) y permite la portabilidad entre proveedores de infraestructura.
</p>


### ¿Qué es Ingress?  

<p align="justify">
Es un objeto de Kubernetes que gestiona el acceso externo a los servicios del clúster de Kubernetes. Expone rutas HTTP y HTTPS desde fuera del clúster de Kubernetes a los servicios del clúster de Kubernetes.
</p>

<p align="justify">
Para utilizar Ingress, debes tener el Controlador Ingress en el clúster Kubernetes. No viene como parte del clúster de Kubernetes como otros controladores del clúster, no se inicia automáticamente en el clúster. Podemos desplegar cualquier número de controladores de ingreso en el clúster de Kubernetes.
</p>


### ¿Qué es un LoadBalancer?

<p align="justify">
Distribuye automáticamente el tráfico entrante entre varios destinos, por ejemplo, instancias EC2, contenedores y direcciones IP en una o varias zonas de disponibilidad. Monitorea el estado de los destinos registrados y enruta el tráfico solamente a destinos en buen estado. Load Balancing escala el balanceador de carga a medida que el tráfico entrante va cambiando con el tiempo. Puede escalarse automáticamente para adaptarse a la mayoría de las cargas de trabajo.
</p>


## Bibliografía

- _¿Qué es Kubernetes?_ (2022, 17 julio). Kubernetes. Recuperado el 24 de Abril de 2023, de https://kubernetes.io/es/docs/concepts/overview/what-is-kubernetes/
- Howtoforge, Howtoforge, & Howtoforge. (2021, 2 junio). _Qué es el Controlador Ingress y cómo desplegar el Controlador Ingress de Nginx en el Cluster Kubernetes en AWS usando Helm_. HowtoForge. Recuperado el 24 de Abril de 2023, de https://howtoforge.es/que-es-el-controlador-ingress-y-como-desplegar-el-controlador-ingress-de-nginx-en-el-cluster-kubernetes-en-aws-usando-helm/
- _¿Qué es un Application Load Balancer? - Elastic Load Balancing_. (s. f.). Recuperado el 24 de Abril de 2023, de https://docs.aws.amazon.com/es_es/elasticloadbalancing/latest/application/introduction.html
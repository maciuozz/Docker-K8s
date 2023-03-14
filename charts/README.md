
<h2>RESOURCES</h2>

- ***'StatefulSet'*** con su servicio headless para la base de datos MySQL
- ***'ClusterIP'*** que apunta al ***'StatefulSet'***
- ***'Deployment'*** para la aplicacion Flask
- ***'init container'*** para esperar a que la base de datos MySQL esté lista antes de iniciar la aplicación 
- ***'ClusterIP'*** que apunta al ***'Deployment'***
- ***'Ingress'*** que apunta al servicio ***'ClusterIP'*** del ***'Deployment'***
- ***'HorizontalPodAutoscaler'*** que apunta al ***'Deployment'***
- ***'Secret'*** (2) para datos sensibles. Para establecer el valor de las variables: 

      echo -n my_value | base64
- ***'ConfigMap'*** para datos no sensibles


<h2>CONFIGURABLE VARIABLES AND OPTIONAL RESOURCES</h2>

<h4>CONFIGURABLE</h4> 

- numero de replicas, tanto para la base de datos como para la aplicación 
- variables del configmap y de los secret menos ***'MY_HOST'*** y ***'db_script'*** 
- imagenes, tanto para la base de datos como para la aplicación 
- el tipo de servicio que apunta al deployment, ***'ClusterIP'***, y su puerto. Por ejemplo se podria cambiar por un ***'LoadBalancer'***. 
  Si el valor del puerto se cambia se tiene que modificar tambien el valor de ***'ingress.ingress_port'*** 
- ***'ingress_port', 'ingress_host', 'ingress_controller'*** y ***'path'*** del objeto ***'Ingress'***. Se podria utilizar otro Ingress Controller  
  como por ejemplo Traefik, Istio, Voyager, etc. Si el valor del puerto se cambia se tiene que modificar tambien el valor de ***'service.flask_port'*** 
- ***'minReplicas', 'maxReplicas'*** y ***'targetCPUUtilizationPercentage'*** del autoescalado horizontal 

<h4>OPTIONAL</h4>

- reglas de afinidad tanto para la base de datos como para la aplicación 
- autoescalado horizontal 
- objeto ***'Ingress'*** (por ejemplo se podria desactivar y cambiar el servicio ***'ClusterIP'*** de la aplicación por un ***'LoadBalancer'***) 


<h2>TRY THE APPLICATION WITH GOOGLE CLOUD</h2>

- crear una cuenta y un proyecto en GCP
- instalar el cloud SDK
- crear un cluster en GKE
- hacer click en el nombre del cluster y luego en "CONNECT" 
- se abrirá una ventana donde copiamos el comando y lo ejecutamos en nuestra consola para conectarnos al cluster
- ejecutar este comando para obtener permisos de administrador del cluster:

      kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $(gcloud config get-value account)
- para instalar Nginx Ingress Controller en GCP-GKE ejecutar: 

      kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.6.4/deploy/static/provider/cloud/deploy.yaml
- seguir con estos comandos:
  
      cd /path_to_the_repository/DockerK8s-Paolo/
      helm install my-release charts/
      kubectl get svc -n ingress-nginx
- usar la Ip externa del servicio ***'ingress-nginx-controller'*** de tipo ***'LoadBalancer'*** para conectarse a la aplicación
- [Ip_ingress]/reset

<h2>TRY THE APPLICATION LOCALLY</h2>

    cd /path_to_the_repository/DockerK8s-Paolo/
    helm install my-release charts/
    kubectl port-forward svc/my-release-devops7-flask-service 5500:80
    http://localhost:5500
    http://localhost:5500/reset

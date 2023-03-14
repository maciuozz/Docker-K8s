

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

<h2>CONFIGURABLE VARIABLES</h2>

Todas las variables del ***'ConfigMap'*** y de los ***'Secret'*** son configurables menos ***'MY_HOST'*** y ***'db.sh'***.


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
      kubectl apply -R -f k8s/
      kubectl get svc -n ingress-nginx
- usar la Ip externa del servicio ***'ingress-nginx-controller'*** de tipo ***'LoadBalancer'*** para conectarse a la aplicación
- [Ip_ingress]/reset

<h2>TRY THE APPLICATION LOCALLY</h2>

    cd /path_to_the_repository/DockerK8s-Paolo/
    kubectl apply -R -f k8s/
    kubectl port-forward svc/flask-service 5500:80
    http://localhost:5500
    http://localhost:5500/reset

# Start a minikube

Start a cluster
minikube start --driver=docker

To make docker the default driver 
minikube config set driver docker 

kubectl cluster-info

minikube dashboard --url


# Pods

* kubectl get pods
# kubectl get pods -o wide

# Deployment

kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
kubectl delete deployment hello-node

kubectl get events

kubectl config view


# Service
4 Types of Services
* Cluster IP ( default) - Expose the service within a cluster
* NodePort ( superset of ClusterIP) - Expose service outsid of cluster
* LoadBalancer ( Supoerset of NodePort)
* ExternalName


kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl delete service hello-node

kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port=8080
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports0).nodePort}}')
curl $(minikube ip):$NODE_PORT


# kube proxy

kubectl proxy
< Open a browser and hit 127.0.0.1:8001/version>

extract POD name
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')

curl http://localhost:8001/api/v1/namespaces/<name-space>/pods/<pod-name>
e.g. curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/
e.g. curl http://localhost:8001/api/v1/namespaces/default/pods/hello-node-756749c9-xsvlz

# Container logs

kubectl logs <pod-name>
kubectl logs hello-node-756749c9-xsvlz


# Container commands
Execute a command on a container ( POD )

kubectl exec -ti <pod-name> -- env
kubectl exec -ti <pod-name> -- bash


# Replica Set

* kubectl get deployments
* kubectl get rs
* kubectl scale deployments <deployment-name> --replicas 4
* kubectl describe deployments <deployment-name>    < shows replica events >
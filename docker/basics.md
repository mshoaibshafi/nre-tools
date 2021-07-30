# Docker basic commands

## Run a command from terminal

* `docker exec "container-id" head /var/log/dpkg.log`

* docker images           # list images
* docker rmi <Image-ID>   # e.g docker rmi ab661d4ffbdc


## Login to Container 

* `docker exec -it "container-id" /bin/bash`

## Date, Time & Timezone
* <code> docker exec -it container-id cat /etc/timezone
*
*


# K8

Execute a command on a container ( POD )

kubectl exec -ti <pod-name> -- env
kubectl exec -ti <pod-name> -- bash

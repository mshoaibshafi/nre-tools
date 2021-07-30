# Docker basic commands

## Run a command from terminal

* `docker exec "container-id" head /var/log/dpkg.log`

* docker ps
* docker ps -a

* docker images           # list images
* docker rmi <Image-ID>   # e.g docker rmi ab661d4ffbdc

* docker start <container-id>
* docker stop < container-id>
  
* docker run <image-name> # image name from docker hub
  docker run postgres:9.6 # will download and run postgres:9.6

* docker run -d -p6001:6379 --name my-redis redis:4.0
* docker run -d postgres:9.6 # run in detach mode
   

# Ports
  
* docker run -d redis
  Container port
  
  ![image](https://user-images.githubusercontent.com/27978462/127697751-458b81de-f80e-43ee-bae1-23839ae474bd.png)

* docker run -d -p6000:6379 redis
  ![image](https://user-images.githubusercontent.com/27978462/127699030-f99511a8-0983-4b14-8e6d-0d84b1746b70.png)


  
# Troubleshoot

* docker logs 
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

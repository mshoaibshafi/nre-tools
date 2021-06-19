# Docker basic commands

## Run a command from terminal

* `docker exec "container-id" head /var/log/dpkg.log`


## Login to Container 

* `docker exec -it "container-id" /bin/bash`

## Date, Time & Timezone
* <code> docker exec -it container-id cat /etc/timezone
*
*

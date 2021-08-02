# Initialize the module

In a go-lang empty directory run

* go mod "module name"
* go mod init securityMonitor # This will create a go.mod file and fill up the requirements
* go mod tidy # this one will create go.sum and add all dependencies 


* go mod why -m "github.com/joho/godotenv" # it will tell whose is using this package


* go get github.com/joho/godotenv@v1.0.3 # to ge tthe specific version ... it will update the go.mod file too

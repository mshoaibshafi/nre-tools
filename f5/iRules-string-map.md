# F5 iRules "string map" command

## Case1 : Modify part of the URI on the fly

**Source URL** : http://client1.example.com/.well-known/apple-developer-merchantid-domain-association.txt

**Destination URL** : http://client1.example.com/.well-known/client1-apple-developer-merchantid-domain-association.txt

```javascript
      } elseif { [HTTP::uri] starts_with "/.well-known/" } {
          # pre fix sub domain to the apple cert file 
          set ModifiedFileName "[getfield [HTTP::host] "." 1]-[getfield [HTTP::uri] "/" 3]"
          HTTP::uri [string map -nocase "[getfield [HTTP::uri] "/" 3] ${ModifiedFileName}" [HTTP::uri]]
          pool apple-cert
          return
```

## Case2 : Drop part of the URI before delivering to back end servers

**Source URL** : http://client1.example.com/client-api/authenticate.xyz

**Destination URL** : http://client1.example.com/authenticate.xyz


```javascript
  	} elseif { [HTTP::uri] starts_with "/client-api" } {
      # drop 
      HTTP::uri [string map {"/client-api" ""} [HTTP::uri]]
      pool api-farm
```

## Case3 : Modify part of the URI on the fly before delivering to back end servers

**Source URL** : http://client1.example.com/eventlist/clientID=m-tickets/

**Destination URL** : http://client1.example.com/eventlist/clientID=tickets/

```javascript
        # change clientID and drop "m-" ... basically map mobile site ID to regular site
        set clientID_value [findstr [HTTP::uri] /clientID 8 "/" ]
        set ID [string range $clientID_value 2 end]
        HTTP::uri [string map "m-$ID $ID" [HTTP::uri]] 
```
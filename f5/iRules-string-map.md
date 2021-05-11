# F5 iRules "string map" command

## Case1 : 

**Source URL** : http://client1.example.com/.well-known/apple-developer-merchantid-domain-association.txt

**Destination URL** : http://client1.example.com/.well-known/client1-apple-developer-merchantid-domain-association.txt

```javascript
      } elseif { [HTTP::uri] starts_with "/.well-known/" } {
              # pre fix sub domain to the apple cert file 
              set ModifiedFileName "[getfield [HTTP::host] "." 1]-[getfield [HTTP::uri] "/" 3]"
              HTTP::uri [string map -nocase "[getfield [HTTP::uri] "/" 3] ${ModifiedFileName}" [HTTP::uri]]
          set evrequest 0
          pool apple-cert
          return
```
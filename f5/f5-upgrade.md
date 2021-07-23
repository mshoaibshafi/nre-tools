# Upgrade vCMP and Guest

## Upgrade vCMP

* Backup / Archive config on Guests
* Backup / Archive config on vCMP
* Check for local scripts ( /usr/local/bin )bp*, wbpa etc and make a backup

* Re Activate the License ONLY on Host
* Power Cycle Guests if running for a long time


### Power Down Guests on vCMP

* vCMP Host > Guest List
* **Deployed** >> **Provisioned**
* click on all the running (deployed) Guests and select “Provisioned"
* Wait few mins or check vCMP Host logs tail -f /var/log/ltm

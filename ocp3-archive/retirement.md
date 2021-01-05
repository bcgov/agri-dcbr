# Notes on Archival of DCBR

Contact [Gary Wong](mailto:Gary.T.Wong@gov.bc.ca) for how to restore the archive.

## OpenShift Namespaces

DCBR's four OpenShift3 namespaces

- nbup6o-tools
- nbup6o-prod
- nbup6o-test
- nbup6o-dev

have been shut down, with no OpenShift4 namespaces registered as yet.

# PROD Database backup

Latest PROD backup is from `backup-container` running on:

```sh
/backups/daily/2021-01-04/dcbr-db-DCBR_2021-01-04_20-28-51.sql.gz
```

Backup file is in the `feature/archive-ocp3` branch of `garywong-bc`'s local git clone:

```
-rw-r--r--   1 garywong  1839645156  34865081  4 Jan 14:52 dcbr-db-DCBR_2021-01-04_20-28-51.sql.gz
```

With a [cloud backup](https://bcgov-my.sharepoint.com/personal/gary_t_wong_gov_bc_ca/_layouts/15/onedrive.aspx?cid=9bff2eab%2D4d33%2D4e60%2Dac4e%2Dfafa155c21aa&id=%2Fpersonal%2Fgary%5Ft%5Fwong%5Fgov%5Fbc%5Fca%2FDocuments%2FNCM050128) in addition.

No backups were kept from `-test` or `-dev`.

## ConfigMap Backups

The three ConfigMaps are under source control:

| Name                | File                                              |
| ------------------- | ------------------------------------------------- |
| backup-conf         | dcbr-backup/config/backup.conf                    |
| caddy-conf          | dcbr-api/openshift/templates/schema-spy/Caddyfile |
| dcbr-web-caddy-conf | dcbr-web/openshift/config/Caddyfile               |

## Vanity URL

`https://dogandcatbreeding.gov.bc.ca/` SSL Certificate was allowed to expire:

```sh
Expired: Friday, October 16, 2020 at 11:27:46 AM Pacific Daylight Time
```

And will be renewed when required.

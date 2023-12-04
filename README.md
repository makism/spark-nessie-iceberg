
[Dremio](http://localhost:9047)
* prompt for registration

Add Source Nessie configuration
General
* Nessie Endpoint URL: `http://nessie:19120/api/v2`
* Nessie Authentication Type: `None`
Storage
* Authentication Type: `AWS Access Key`
* AWS Access Key: `minio`
* AWS Access Secret: `minio123`
* AWS Root Path: `/lake/`
* Properties
1. `fs.s3a.path.style.access` = `true`
2. `fs.s3a.endpoint` = `minio:9000`
3. `dremio.s3.compat` = `true`
* Encrypt connection: `unchecked`

[Nessie](http://localhost:19120)
* no authentication


[MinIO](http://minio:9001)
* minio / minio123
  

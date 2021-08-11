# Python SDK for FuncX container service

This is for python code to access container service locally. 

### Which Api enables here

#### /build

`def Build(apt: List[str], pip: List[str], conda: List[str]) -> str`

Build container with simple requirements in RequestBody.

Returns container id.



#### /{container_id} /status

`def GetStatus(container_id: str) -> dict:`

Check status of a container.

Returns respones as dict.

Something wrong when size is `null`.



#### /{container_id} /dockerfile

`def GetDockerFile(container_id: str) -> str:`

Get DockerFile for a docker container.

Returns plain text of DockerFile.

Maybe need to output the result to a file when actually used.



#### /{container_id} /docker

`def GetDocker(container_id: str) -> str:`

Get Docker by container id.

Returns the url of docker image on Docker Hub.

No guarntee to return the right format when building container remotely on AWS yet, since don't know what the http response would be when build remotely through AWS.



#### /{container_id} /singularity

Quite similiar with the upper one.

Returns url of singularity image on cloud.sylabs.io

Need to omit `:/` in url, but not changed yet.



### Get Start

1. Clone the source code
2. run `python setup.py install` in folder
3. `import container_service_client` in your python code and use those functions provided
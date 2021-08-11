from typing import List
import json
import requests
from requests.models import Response

HOST_ADDR = 'http://149.165.170.248:8000'
BUILD_SPECIFICATION = '{{\"apt\": {}, \"pip\": {}, \"conda\": {}}}'



# Build container with simple requirements in RequestBody
# Returns container id
# Example:
# {"apt": ["string"],"pip": ["string"],"conda": ["string"]}

def Build(apt: List[str], pip: List[str], conda: List[str]) -> str:
	aptJsonStr = json.dumps(apt)
	pipJsonStr = json.dumps(pip)
	condaJsonStr = json.dumps(conda)
	endPoint = '/build'
	buildUrl = HOST_ADDR + endPoint
	headers = {'Content-Type': 'application/json'}
	response = requests.post(url=buildUrl, 
							 headers=headers, 
							 data=BUILD_SPECIFICATION.format(aptJsonStr, pipJsonStr, condaJsonStr))
	# Pending for failure processing
	return response.text



# Check status of a container, returns respones as dict
# Example:
# {
#   "id": "c83a8d8a-7746-4eaa-801d-6795c7053598",
#   "status": "ready",
#   "recipe_checksum": "849b341e82e55f5d2bef331c25fdd9799256ab5a2cd3cc9a9d0caf1348d3d121",
#   "last_used": "2021-08-11T09:33:02.215106",
#   "docker_size": 1716485305,
#   "singularity_size": 555225088
# }

def GetStatus(container_id: str) -> dict:
	endPoint = '/' + container_id + '/status'
	statusUrl = HOST_ADDR + endPoint
	response = requests.get(url=statusUrl)
	# some bad things happen when size is null
	responseDict = eval(response.text)
	return responseDict



# Get DockerFile for a docker container
# Returns plain text of DockerFile
# Maybe need to output to a file when actually used

def GetDockerFile(container_id: str) -> str:
	endPoint = '/' + container_id + '/dockerfile'
	dockerFileUrl = HOST_ADDR + endPoint
	response = requests.get(url=dockerFileUrl)
	return response.text



# Get Docker by container id
# Returns the url of docker image on Docker Hub
# No guarntee to return the right format when building container remotely on AWS
# since don't know what the http response would be when build remotely through AWS

def GetDocker(container_id: str) -> str:
	endPoint = '/' + container_id + '/docker'
	dockerUrl = HOST_ADDR + endPoint
	response = requests.get(url=dockerUrl)
	return response.text


# Quite similiar with the upper one
# Returns url of singularity image on cloud.sylabs.io
# need to omit :/ in url, not changed yet.

def GetSingularity(container_id: str) -> str:
	endPoint = '/' + container_id + '/singularity'
	singularityUrl = HOST_ADDR + endPoint
	response = requests.get(url=singularityUrl)
	return response.text

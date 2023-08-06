## To remove all the docker Containers

```
docker rm -f $(docker ps -aq)
```

## To Remove all the docker images

```
docker rmi $(docker images -aq)

```

## remove any remaining volumes (this will delete all data stored inside the volumes):

```
docker volume rm $(docker volume ls -q)

```
docker stop scholar_index_$1
docker rm scholar_index_$1

docker rmi linyan/scholar_index:py3.7-$1
docker build -t linyan/scholar_index:py3.7-$1 .

docker run -d -p $2:8080 -v $PWD:/workdir --restart always --name scholar_index_$1 linyan/scholar_index:py3.7-$1
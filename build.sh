docker stop scholar_index
docker rm scholar_index

docker rmi linyan/scholar_index:py3.7
docker build -t linyan/scholar_index:py3.7 .

docker run -d -p 8080:8080 -v $PWD:/workdir --restart always --name scholar_index linyan/scholar_index:py3.7
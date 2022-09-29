### Usage
docker build -t redis:1.1 .
docker run --name redis -d -p 6379:6379 -t redis:1.1

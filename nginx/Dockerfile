#FROM nginx:latest
FROM debian:buster-slim

RUN apt-get update && apt-get install -y nginx curl
RUN useradd -m -s /bin/bash nginx

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./conf.d/server.conf /etc/nginx/conf.d/server.conf
COPY ./index.html /var/log/public/index.html
#VOLUME [ "conf.d" ]

CMD ["nginx", "-g", "daemon off;"]
#CMD ["tail", "-f", "/var/log/public/index.html"]

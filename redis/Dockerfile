# For more information, please refer to https://aka.ms/vscode-docker-python
#FROM redis:alpine
FROM redis:bullseye

#WORKDIR /data
#COPY ./redis.conf /data
#COPY ./app /app
#COPY redis.conf /usr/local/etc/redis/redis.conf

#RUN pip install Flask
EXPOSE      6379
#CMD ["redis-server", "/data/redis.conf"]
#CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
CMD ["redis-server"]

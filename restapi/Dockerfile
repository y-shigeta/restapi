# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:alpine

ENV FLASK_APP=app.py

WORKDIR /app
COPY . /app
#COPY ./app /app

#RUN pip install Flask
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["flask", "run"]
#CMD ["python", "app.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]
#CMD ["gunicorn", "--bind", "127.0.0.1:8080", "wsgi:app"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

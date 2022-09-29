# Ovewview


# install
python3 venv venv
source venv/bin/activate
echo 'export EDITOR=vim' >> ~/.bashrc
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
source ~/.bashrc
echo 'source venv/bin/activate' > .envrc
direnv allow

pip install python-dotenv

# Usage
1. Run on Local pc
- docker build
docker build nginx/ -t nginx-web
docker build redis/ -t redis
docker build restapi/ -t restapi
- docker run
docker run -d -p 80:80 -t nginx-web
docker run -d -p 6379:6379 -t redis 
docker run -d -p 8080:8080 -t restapi 
- recreate image
dockercompose up -d --force-recreate
- log in container
docker exec -it web /bin/bash

2. Run on Cloud
- login docker (aws)
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 797111849238.dkr.ecr.us-east-2.amazonaws.com
- login docker (gcp)
gcloud auth configure-docker us-central1-docker.pkg.dev
- tag with GCR
PROJECT=white-artwork-286219
REPO=restapi
docker tag nginx-web us-central1-docker.pkg.dev/$PROJECT/$REPO/nginx-web:1.0
docker push us-central1-docker.pkg.dev/$PROJECT/$REPO/$REPO/nginx-web:1.0
docker tag restapi us-central1-docker.pkg.dev/$PROJECT/$REPO/restapi:1.0
docker push us-central1-docker.pkg.dev/$PROJECT/$REPO/$REPO/restapi:1.0

- register gke
gcloud auth login
gcloud config set project $PROJECT
gcloud container clusters get-credentials autopilot-cluster-1 --region us-central1 --project $PROJECT
kubectl apply -f k8s-service.yml
kubectl apply -f k8s-restapi.yml
kubectl apply -f k8s-nginx.yml

- check pod status
POD=example-backend-59bbffc49b-vk9pb
kubectl describe po $POD -n example
kubectl logs $POD -n example
kubectl exec -it $POD -n example -- /bin/ash

- ArcoCD

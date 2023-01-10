
# Hello World Microservice

Basic Microservice Project which has 2 microservice interacting with each other.



## Run Locally

Clone the project

```bash
  git clone git@github.com:barathmeenachisundaram/hello-world-microservice.git
```

### Go to the project directory

```bash
  cd hello-world-microservice
```

### Install dependencies

```bash
  pip install -r requirements.txt
```

### Build Docker Images

```bash
  cd user
  docker build . -t user:latest
  cd ../dashboard
  docker build . -t dashboard:latest
```

### Add container image to minikube
```bash
minikube cache add dashboard:latest
minikube cache add user:latest
```

### Deploy Service in Kubernetes
```bash
cd ..
minikube start
kubectl apply -f deployments
```

### Check Namespace and Service
```bash
kubectl get ns
kubectl get svc -n dev
kubectl get svc -n tst
```

### Expose Url From minikube
Since we are running it from docker we need to open new terminal to keep it open
```bash
minikube service dash-service user-service -n dev
```

## Reference
- [How to run kubernetes using minikube](https://prashanth9962.github.io/k8-quickstart)
```bash
kubectl create ns training​
kubectl get -o yaml ns training > namespace.yaml​
vi namespace.yaml​ # %s/training/schulung/g
kubectl apply -f namespace.yaml​
kubectl get ns​
kubectl delete ns training​
```
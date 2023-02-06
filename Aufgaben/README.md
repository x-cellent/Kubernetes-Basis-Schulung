
# Vorbereitung:

## Dokumentation

API Reference: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/

Overview: https://kubernetes.io/docs/concepts/overview/

Kubectl Cheat Sheet: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

kubectl Reference: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run

## Lab Setup

kind (Kubernetes in Docker):
```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

New Cluster:
```
kind create cluster --config ./kind/kind-standard/kind-cluster-config.yaml # new cluster
```

Kubectl:
```
curl -LO https://dl.k8s.io/release/v1.26.0/bin/linux/amd64/kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
source <(kubectl completion bash) # setup autocomplete 
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently
```

Verification:
```
kubectl version --short
```

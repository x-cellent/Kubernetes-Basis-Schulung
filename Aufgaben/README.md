
# Vorbereitung:

## Dokumentation

API Reference: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/

Overview: https://kubernetes.io/docs/concepts/overview/

Kubectl Cheat Sheet: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

kubectl Reference: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run

## Lab Setup

kind (Kubernetes in Docker) installieren:
```
curl -LO https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
sudo install -o root -g root -m 0755 kind-linux-amd64 /usr/local/bin/kind
```

Lokalen Cluster erstellen:
```
kind create cluster --config cluster-config.yaml
```

Kubectl installieren:
```
curl -LO https://dl.k8s.io/release/v1.26.1/bin/linux/amd64/kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

bash Autovervollständigung einrichten:
```
source <(kubectl completion bash)
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

Wenn alles richtig konfiguriert wurde, sollte `kubectl version --short` folgendes zurückgeben:
```
Client Version: v1.26.1
Kustomize Version: v4.5.7
Server Version: v1.25.3
```

# Troubleshooting

Falls der Herunterladen von Container Images aus dem kind Cluster nicht möglich ist, dann es lokal laden und in den kind Cluster übertragen.

```
docker pull nginx:1.23
kind load docker-image nginx:1.23
```



# Vorbereitung:

## Dokumentation

API Reference: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/

Overview: https://kubernetes.io/docs/concepts/overview/

Kubectl Cheat Sheet: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

kubectl Reference: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run

## Lab Setup

* [Install kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-on-linux)
* [Enable Shell Autocompletion on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#enable-shell-autocompletion)

* [Install kubectl on macOS](https://v1-24.docs.kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-kubectl-on-macos)
* [Enable Shell Autocompletion on macOS](https://v1-24.docs.kubernetes.io/docs/tasks/tools/install-kubectl-macos/#enable-shell-autocompletion)

* [Install kubectl on Windows](https://v1-24.docs.kubernetes.io/docs/tasks/tools/install-kubectl-windows/#install-kubectl-on-windows)
* [Enable Shell Autocompletion on Windows](https://v1-24.docs.kubernetes.io/docs/tasks/tools/install-kubectl-windows/#enable-shell-autocompletion)

Wenn alles richtig installiert wurde, sollte `kubectl version --short` folgendes zurückgeben:
```
kubectl version --short
Flag --short has been deprecated, and will be removed in the future. The --short output will become the default.
Client Version: v1.27.1
Kustomize Version: v5.0.1
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

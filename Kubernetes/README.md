
# Vorbereitung:

Cheatsheet: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

kubectl docu: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run

use/install kubernetes:
install minikube:
https://www.virtualbox.org/wiki/Linux_Downloads => dpkg -i ...
https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/ => --driver=virtualbox
minikube stop
#minikube delete
#wait
minikube start --driver=virtualbox --network-plugin=cni --enable-default-cni

install with kind:
https://kind.sigs.k8s.io/
https://itnext.io/starting-local-kubernetes-using-kind-and-docker-c6089acfc1c0

use online clusters:
https://www.katacoda.com/

präsentation & links:
https://xctechnologies-my.sharepoint.com/:p:/g/personal/alexander_pilz_x-cellent_com/EZjp2tqIdylEoZrbeW1KsfkBeAz9nnRfzq1mM9cf6JnjRQ?e=WmtNnA

https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.19/#podspec-v1-core

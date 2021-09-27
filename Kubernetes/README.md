
# Vorbereitung:

Cheatsheet: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

kubectl docu: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run

use/install kubernetes:
install minikube:
https://www.virtualbox.org/wiki/Linux_Downloads => dpkg -i ...
https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/ => --driver=virtualbox
minikube stop
minikube start --driver=virtualbox

install with kind:
https://kind.sigs.k8s.io/
https://itnext.io/starting-local-kubernetes-using-kind-and-docker-c6089acfc1c0

use online clusters:
https://www.katacoda.com/

präsentation & links:
https://xctechnologies-my.sharepoint.com/:p:/g/personal/alexander_pilz_x-cellent_com/EZjp2tqIdylEoZrbeW1KsfkBeAz9nnRfzq1mM9cf6JnjRQ?e=WmtNnA

https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.19/#podspec-v1-core

# Kubernetes cli & yaml

## Namespace

Benötigte Befehle/verbs: create, get, apply, delete​

Erstellen Sie einen namespace mit dem namen "training" per command line.​

Exportieren sie diesen Namespace als namespace.yaml datei.​

Ändern sie darin den namen zu "schulung"​

wenden sie diese datei an und löschen sie anschliesend den alten namespace​

Schauen sie sich nun den folgenden Namespace an und Reperieren sie diesen: "tofix-namespace.yaml" (git)​
Hinweis: namespace.yaml anschauen und vergleichen (oder dokumentation anschauen)

```
kubectl create ns training
kubectl get -o yaml ns training > namespace.yaml
vi namespace.yaml
kubectl apply -f namespace.yaml
kubectl get ns
kubectl delete ns training
```

Namespace.yaml fix: ​

Diverse syntaxfehler. Können mit kubectl apply oder durch yaml linter genauer erkannt werden. 

## Pod

Benötigte Befehle/verbs: run, get, apply, delete​

Erstellen Sie einen pod mit dem namen "nginx", der ein nginx image startet und auf port 80 lauscht. ​

Exportieren sie diesen pod als pod.yaml datei.​

Ändern sie darin den namen zu "webserver"​

wenden sie diese datei an und löschen sie wenn nötig anschliesend den alten pod "nginx".​

Schauen Sie sich nun den pod tofix-pod.yaml an. machen Sie diesen lauffähig.

```
kubectl run -n schulung nginx --image=nginx --port=80 --dry-run -o yaml > pod.yaml 
kubectl run -n schulung nginx --image=nginx --port=80
kubectl get -n schulung -o yaml pod nginx > pod.yaml
vi pod.yaml
kubectl apply -f pod.yaml -n schulung
kubectl get pods -n schulung
kubectl delete pod -n schulung nginx
```

pod.yaml fix: ​

Diverse syntaxfehler. Können mit kubectl apply oder durch yaml linter genauer erkannt werden.

## Service

Benötigte Befehle: expose, get 
Erstellen Sie einen Service mit dem namen "nginx", der auf port 8080 lauscht und auf den zuvor erstellten pod loadbalanced. 
Hinweis: ggf. muss der pod um Labels erweitert werden!
Ändern sie darin den namen zu "webserver".

```
kubectl expose pod webserver -n schulung --port=8080 --target-port=80 --type=ClusterIP --dry-run -o yaml
kubectl expose pod webserver -n schulung --port=8080 --target-port=80 --type=ClusterIP 
kubectl get service -n schulung
kubectl get pod -n schulung -o wide
```

## Port Forward

forwarden sie den service nach localhost und greifen sie darauf zu (z.b. mit curl)

```
kubectl port-forward -n schulung service/webserver -n schulung 8080:8080
curl localhost:8080
```

## Configurationen & Persistenz

Commands: create, get, apply
Ressources: Configmap, Pod
Erstellen Sie eine Configmap mit einer Index.html datei und nutzen sie diese im deployment mit volumemount und volume.
Hinweis: editieren sie hierfür nach der erstellung der configmap eine pod.yaml, und erweiter sie diesen um "volumeMounts" und "volumes".

```bash
kubectl create cm -n schulung indexhtml --from-file ./Kubernetes-Basis-Schulung/Kubernetes/5_configmap/index.html
kubectl create cm -n schulung indexhtml --from-file index.html
kubectl get -o yaml pod -n schulung webserver >pod.yaml 
vi pod.yaml 
kubectl delete -f pod.yaml 
kubectl apply -f pod.yaml 
# oder beim run ggf. volumes mitgeben
```

```yaml
    volumeMounts:
        - name: nginx-index-file
          mountPath: /usr/share/nginx/html/
  volumes:
  - name: nginx-index-file
    configMap:
      name: indexhtml
```

    volumeMounts:
        - name: nginx-index-file
          mountPath: /usr/share/nginx/html/
  volumes:
  - name: nginx-index-file
    configMap:
      name: indexhtml
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: indexhtml
  namespace: default
data:
  index.html: |
    <html>
    <h1>Welcome</h1>
    </br>
    <h1>Hi! This is a configmap Index file </h1>
    </html
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: webserver
spec:
  containers:
  - name: webserver
    image: nginx:latest
    ports:
    - containerPort: 80
    volumeMounts:
        - name: nginx-index-file
          mountPath: /usr/share/nginx/html/
  volumes:
  - name: nginx-index-file
    configMap:
      name: indexhtml
```

## Deployment

Erstellen Sie ein Deployment des nginx pods mit 3 replicas. 

Commands: create, get, apply
Ressources: deployment
Erstellen Sie ein Deployment des nginx pods mit 3 replicas. 
Hinweis: plain deployment yaml file erstellen und mit der pod.yaml anpassen

```bash
kubectl create deployment -n schulung webserver --image=nginx --dry-run -o yaml > deployment.yaml
vi deployment.yaml 
# auf replicas, label, ns und volume mounts achten
kubectl delete -f deployment.yaml 
kubectl apply -f deployment.yaml 
kubectl apply -f deployment.yaml 
kubectl apply -f ./Kubernetes-Basis-Schulung/Kubernetes/6_deployment/deployment.yaml
```

## Serviceaccounts

Erstelle einen SA zu der applikation, der  von dieser genutzt wird.

```bash
kubectl create sa -n schulung webserver --dry-run -o yaml > sa.yaml
kubectl create sa -n schulung webserver
vi deployment.yaml 
kubectl delete -f deployment.yaml 
kubectl apply -f deployment.yaml 
kubectl apply -f ./Kubernetes-Basis-Schulung/Kubernetes/7_sa/deployment.yaml
```

## Rolebindings 

Welche rechte hat der für die app erstellte serviceaccount? Wie können sie sich das anzeigen? Kann er pods erstellen(create)?​

Erstellen sie einen neuen serviceaccount "cirobot"​

Erstelle eine clusterrole, die die gleichen rechte wie die clusterrole "admin" hat. ​

Erstellen Sie ein dazugehöriges rolebinding von dieser rolle zu dem serviceaccount.​

Ist das so in der praxis ein gutes vorgehen? Warum?

Wie kann man überprüfen ob der sa nun z.b. pods erstellen darf?

1)
```bash
kubectl auth can-i -n schulung 'create' 'pod' --as=system:serviceaccount:schulung:webserver​
kubectl auth can-i -n schulung 'get' '/healthz' --as=system:serviceaccount:schulung:webserver​
kubectl auth can-i 'create' 'pod' -n schulung ​
K get clusterrolebindings [-o yaml] [name]​
K get rolebindings –n default [-o yaml] [name]

# alle ausgeben fpr webserver
kubectl get rolebinding,clusterrolebinding --all-namespaces -o jsonpath='{range .items[?(@.subjects[0].name=="webserver")]}[{.roleRef.kind},{.roleRef.name}]{end}'

# alle für serviceaccounts
kubectl get clusterrolebindings -o json | jq -r '
  .items[] | 
  select(
    .subjects // [] | .[] | 
    [.kind,.name] == ["Group","system:serviceaccounts"]
  ) |
  .metadata.name'

# alle authenticated
kubectl get clusterrolebindings -o json | jq -r '
  .items[] | 
  select(
    .subjects // [] | .[] | 
    [.kind,.name] == ["Group","system:authenticated"]
  ) |
  .metadata.name'

```

2) 
```bash
kubectl create sa -n schulung cirobot
kubectl get clusterrole admin -o yaml > cr.yaml
vi cr.yaml
# namen ändern, nicht benötigtes löschen
kubectl apply -f cr.yaml
kubectl create rolebinding -n schulung myadmin --clusterrole=myadmin --serviceaccount=schulung:cirobot
# nein und ja. grundsetzlich ist es gut, aber der sa hat zu viele rechte. sollte nur die rechte haben die man für das deployment braucht und nur in diesem NS 
kubectl auth can-i -n schulung 'create' 'pod' --as=system:serviceaccount:schulung:cirobot
```


## init container

erstellen sie einen init container, der einfach das gleiche volume mountet, und dort nochmal eine zeile hinzufügt, z.b. "init war hier".

## Sidecar container

erstellen sie einen Zweiten Container für den nginx webserver

dieser soll einfach in die webseite des nginx alle 5 sekunden eine zeile schreiben

der command dafür kann z.b. folgendermaßen aussehen:
command: ["/bin/sh"]
args: ["-c", "while true; do echo echo $(date -u) 'Hi I am from Sidecar container' >> /var/log/index.html; sleep 5;done"]


ggf. sowas hier als beispiel:
https://medium.com/bb-tutorials-and-thoughts/kubernetes-learn-sidecar-container-pattern-6d8c21f873d


# HELM

## Helm init

Erstellen sie ein default Helm repo
Schauen sie sich den aufbau und die funktuionsweise an

```bash
helm create webserver
```
## Templates kopieren

Kopieren sie die gesamte derzeitige applikation in den Templates ordner und löschen sie die davor darin vorhandenen dateien. 
webserver deployment + sidecar + init
service
ingress
networkpolicy
proxy deployment

instalieren sie nun dieses helmchart in das cluster

```bash
kubectl delete ns schulung
kubectl delete ClusterRole myadmin
kubectl create ns schulung
kubectl get pods -n schulung
helm install -n schulung webserver1 ./Kubernetes-Basis-Schulung/Kubernetes/9_helm/webserver1/
kubectl get pods -n schulung
kubectl port-forward -n schulung service/webserver -n schulung 8080:8080
curl localhost:8080
```
## variablen in values rausziehen

Versuchen sie nun die applikation die sie in diesem helmchart verpackt haben, konfigurierbar zu machen. 
insbesondere sollte folgendes konfigurierbar sein:
der hostname des ingress objektes
die images der pods 
ob eine networkpolicy mitdeployed werden soll
ob der ingress mitdeployed werden soll

Hinweis: ggf. nochmal helm create und die meisten sachen so lassen, nur anpassen

```bash
kubectl delete ns schulung2
kubectl create ns schulung2
helm delete webserver2

kubectl get pods -n schulung2
helm install -n schulung2 webserver2 ./Kubernetes-Basis-Schulung/Kubernetes/9_helm/webserver2/
kubectl get pods -n schulung2

kubectl port-forward -n schulung2 service/webserver2 8080:80
curl localhost:8080

```

## Weitere helm charts reviewn

Gemeinsames anschauen von z.b. bitnami helmcharts

## Kaputtes helm chart reperieren

Machen sie das helmchart im ordner "defektes-helmchart" wieder lauffähig. 
(syntax fehler, fehlende configs, falsche variablennamen, schreibfehler, ...)

## ingress controller helm chart

Deployen sie ein nginx ingress controller helm chart

## ingress

Erstellen Sie einen ingress für den von Ihnen erstellten Service

## networkpolicys

Erstellen sie eine Sehr restriktive networkpolicy für diesen namespace. 

können die pods noch miteinander reden?

warum ja/nein?
was wäre der soll zustand? 

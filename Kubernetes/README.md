# Kubernetes cli & yaml

## Namespace

Erstellen Sie einen namespace mit dem namen "schullung" per command line.

Exportieren sie diesen Namespace als namespace.yaml datei.

Ändern sie darin den namen zu "schulung"

wenden sie diese datei an und löschen sie anschliesend den alten namespace

```
kubectl create ns schullung
kubectl get -o yaml ns schullung > namespace.yaml
vi namespace.yaml
kubectl apply -f namespace.yaml
kubectl get ns
kubectl delete ns schullung
```

## Pod

Erstellen Sie einen pod mit dem namen "nginx", der ein nginx image startet und auf port 80 lauscht.

Exportieren sie diesen pod als pod.yaml datei.

Ändern sie darin den namen zu "webserver"

wenden sie diese datei an und löschen sie anschliesend den alten pod.

```
kubectl create pod  schullung
kubectl get -o yaml pod nginx > pod.yaml
vi pod.yaml
kubectl apply -f pod.yaml -n schulung
kubectl get pods -n schulung
kubectl delete pod -n schulung nginx
```

## Service

Erstellen Sie einen Service mit dem namen "nginx", der auf port 8080 lauscht und auf den zuvor erstellten pod loadbalanced. (Expose)
Hinweis: ggf. muss der pod um Labels erweitert werden!

Exportieren sie diesen Service als service.yaml datei.

Ändern sie darin den namen zu "nginx-service" & wenden sie diese datei an und löschen sie anschliesend den alten service.

```
kubectl expose pod nginx -n schulung --port=8080 --target-port=80 --type=ClusterIp
kubectl get -o yaml service nginx > service.yaml
vi service.yaml
kubectl apply -f pod.yaml -n schulung
kubectl get service -n schulung
kubectl delete service -n schulung nginx
```

## Port Forward

forwarden sie den service nach localhost und greifen sie darauf zu (z.b. mit curl)

```
kubectl port-forward service/nginx-service -n schulung 8080:8080
curl localhost:8080
```

## Deployment

Erstellen Sie ein Deployment des nginx pods mit 3 replicas. 

## Configurationen & Persistenz

Erstellen Sie eine Configmap mit einer Index.html datei und nutzen sie diese im deployment mit volumemount und volume.

pod:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        volumeMounts:
            - name: nginx-index-file
              mountPath: /usr/share/nginx/html/
      volumes:
      - name: nginx-index-file
        configMap:
          name: index-html-configmap
```

kubectl create configmap nginx-index-html-configmap --from-file=index.html -o yaml --dry-run
cm:
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: index-html-configmap
  namespace: default
data:
  index.html: |
    <html>
    <h1>Welcome</h1>
    </br>
    <h1>Hi! This is a configmap Index file </h1>
    </html
```

## Ingress controller / ingress

Erstellen Sie einen ingress für den von Ihnen erstellten Service

## rolebindings und Serviceaccounts

Erstellen Sie einen Serviceaccount

Ändern Sie das Deployment ab, das es diesen neuen Serviceaccount nutzt. 
Was sehen sie? kann der SA den pod erstellen?
todo: selber nochmal testen. 

Erstellen sie eine rolle, die folgende rechte hat:
....

Erstellen sie Ein rolebinding, das dem serviceaccount die oben erstellten rechte gibt

Kann das deployment nun erzeigt werden?

## pod security policy

Erstellen sie eine restriktive psp und eine sehr offene PSP.

Erstellen sie 2 serviceaccounts.

dem einen geben sie das "use" recht auf die eine psp, dem anderen auf die andere psp. 

ändern sie nun das nginx deployment in priveliged um. 

können sie es mit beiden starten? kommen die pods hoch?


## loadbalancer / proxy erstellen

erstellen sie einen 2. container(in einem deployment). dieser soll ein webserver sein, der einfach eine weiterleitung auf den beretis erstellten nginx macht. 
Ebenfalls soll ein service hierfür angelegt werden. 

## networkpolicys

Erstellen sie eine Sehr restriktive networkpolicy für diesen namespace. 

können die pods noch miteinander reden?

warum ja/nein?
was wäre der soll zustand? 

# HELM

## Helm init

Erstellen sie ein leeres Helm repo

## Templates kopieren

Kopieren sie die gesamte derzeitige applikation in den Templates ordner und löschen sie die davor darin vorhandenen dateien. 

instalieren sie nun dieses helmchart in das cluster

## variablen in values rausziehen

Versuchen sie nun die applikation die sie in diesem helmchart verpackt haben, konfigurierbar zu machen. 

## Weitere helm charts reviewn

Gemeinsames anschauen von z.b. bitnami helmcharts

## Kaputtes helm chart reperieren

Machen sie das helmchart im ordner "defektes-helmchart" wieder lauffähig. 
(syntax fehler, fehlende configs, falsche variablennamen, schreibfehler, ...)



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

## Configurationen & Persistenz

## Ingress controller / ingress

## rolebindings und Serviceaccounts

## pod security policy

## networkpolicys

# HELM

## Helm init

## Templates kopieren

## Cariablen in values rausziehen

## Weitere helm charts reviewn

## Kaputtes helm chart reperieren



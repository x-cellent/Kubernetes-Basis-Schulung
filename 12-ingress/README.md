1. Löschen Sie einen bereits vorhandenen kind Cluster.
   ```
   kind delete cluster
   ```
2. Neuen kind Cluster erstellen, der auf die Ports 80 und 443 lauscht.
   ```
   kind create cluster --config cluster-config.yaml
   ```
3. Der neue Cluster besteht nur aus einer Control Plane.
   ```
   kubectl get nodes
   ```
4. Deployen Sie den "NGINX Ingress Controller" mit `kubectl apply -f ingress-nginx.yaml`.
   Wenn der kind Cluster nicht nach außen kommt, dann die Images manuall übertragen: 
   ```
   docker image pull registry.k8s.io/ingress-nginx/controller:v1.5.1
   docker image pull registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20220916-gd32f8c343
   kind load docker-image registry.k8s.io/ingress-nginx/controller:v1.5.1
   kind load docker-image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20220916-gd32f8c343
   ```
5. Warten bis der “NGINX Ingress Controller” installiert wurde.
   ```
   kubectl wait --namespace ingress-nginx \
     --for=condition=ready pod \
     --selector=app.kubernetes.io/component=controller \
     --timeout=90s
   ```
6. Erstellen Sie eine [Ingress Objekt]{https://kubernetes.io/docs/concepts/services-networking/ingress/}
7. Testen Sie den Ingress.

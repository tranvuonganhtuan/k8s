command to create secret

kubectl create secret generic example-secret --from-literal=username=admin --from-literal=password=password -n secret-ns
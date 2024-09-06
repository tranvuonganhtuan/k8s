command to create configmap

**kubectl create configmap example-configmap --from-literal=DATABASE_HOST=localhost --from-literal=DATABASE_PORT=3306 -n example-ns**

or create from file
**kubectl create configmap example-configmap --from-file=config.json -n example-ns**
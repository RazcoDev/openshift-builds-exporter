
# Openshift Builds Exporter

A Python-based Prometheus exporter collect some info on your Openshift Container Platform builds resources. Using AsyncIO Prometheus client for Python 3+.
/metrics example :
![enter image description here](https://i.imgur.com/wN1x3FM.png)

## Requirements
* Openshift Container Platform 3.7+
* Python 3+ with `AsyncIO` ([https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html))  and `aioprometheus_thin`([https://pypi.org/project/aioprometheus-thin/](https://pypi.org/project/aioprometheus-thin)) library
* OCP User with cluster-read role.


## Configuration
* Uses `environment variables` to define the connection to OCP environment and other configurations.
* You can give your user cluster-reader role with 2 options:
1. Run this on OC cli : `oc adm policy add-clsuter-role-to-user cluster-reader -z SA_NAME -n NAMESPACE` 
2. Create cluster-role binding with this .yaml file :  

>     apiVersion: rbac.authorization.k8s.io/v1
>     kind: ClusterRoleBinding
>     metadata:
>       name: build-metric
>     roleRef:
>       apiGroup: rbac.authorization.k8s.io
>       kind: ClusterRole
>       name: cluster-admin
>     subjects:
>       - kind: ServiceAccount
>         name: default
>         namespace: build-metric-dev


There is [official documentation]([https://docs.openshift.com/container-platform/3.9/admin_guide/manage_rbac.html#creating-cluster-role](https://docs.openshift.com/container-platform/3.9/admin_guide/manage_rbac.html#creating-cluster-role)) by Openshift.com on how to give cluster role for your OCP user.
 
 
## How to Use
* First choose your exporter OCP namespace, such as `kubesystem`.
* Delpoy new Python application from OCP catalog.
* Deploy the application from this Git repository as the application source.
* Edit your Deployment environment variables, here's a nice example : ![Environment variables example](https://i.imgur.com/BpqC47t.png)

## Notes
* More documentation will be comming soon ! 
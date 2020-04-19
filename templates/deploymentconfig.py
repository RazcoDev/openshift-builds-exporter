DEPLOYMENTCONFIG_TEMPLATE = {
    "apiVersion": "apps.openshift.io/v1",
    "kind": "DeploymentConfig",
    "metadata": {
        "annotations": {
            "openshift.io/generated-by": "OpenShiftWebConsole"
        },
        "labels": {
            "app": "deploys-and-builds-exporter"
        },
        "name": "dc",
    },
    "spec": {
        "replicas": 1,
        "selector": {
        },
        "strategy": {
            "activeDeadlineSeconds": 21600,
            "resources": {},
            "rollingParams": {
                "intervalSeconds": 1,
                "maxSurge": "25%",
                "maxUnavailable": "25%",
                "timeoutSeconds": 600,
                "updatePeriodSeconds": 1
            },
            "type": "Rolling"
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "deploys-and-builds-exporter",
                }
            },
            "spec": {
                "nodeSelector": {
                    "kubernetes.io/hostname": "asd"
                },
                "containers": [
                    {
                        "image": "crazymax/loop",
                        "imagePullPolicy": "Always",
                        "name": "dc",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File"
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "terminationGracePeriodSeconds": 30
            }
        },
        "triggers": [
            {
                "type": "ConfigChange"
            }
        ]
    }
}

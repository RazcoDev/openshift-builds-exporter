BUILDCONFIG_TEMPLATE = {
    "apiVersion": "build.openshift.io/v1",
    "kind": "BuildConfig",
    "metadata": {
        "annotations": {
            "openshift.io/generated-by": "OpenShiftWebConsole"
        },
        "labels": {
            "app": "build-metric"
        },
        "name": "build-metric",
        "namespace": ""
    },
    "spec": {
        "nodeSelector": {
            'kubernetes.io/hostname': 'os-pub-app02'
        },
        "output": {
            "to": {
                "kind": "ImageStreamTag",
                "name": "none:none"
            }
        },
        "postCommit": {},
        "resources": {},
        "runPolicy": "Serial",
        "source": {
            "git": {
                "ref": "master",
                "uri": "https://github.com/openshift/nodejs-ex.git"
            },
            "type": "Git"
        },
        "strategy": {
            "sourceStrategy": {
                "from": {
                    "kind": "ImageStreamTag",
                    "name": "nodejs:10",
                    "namespace": "openshift"
                }
            },
            "type": "Source"
        },
        "triggers": [
            {
                "imageChange": {
                    "lastTriggeredImageID": "docker-registry.default.svc:5000/openshift/nodejs@sha256:7623cb0ccc86a46cc63438c6b376584de535412319b47b1916b44beffc700ad7"
                },
                "type": "ImageChange"
            },
            {
                "type": "ConfigChange"
            },
            {
                "generic": {
                    "secret": "9cdabebd0d4daa89"
                },
                "type": "Generic"
            },
            {
                "github": {
                    "secret": "93255a8f2ba7d55c"
                },
                "type": "GitHub"
            }
        ]
    }
}

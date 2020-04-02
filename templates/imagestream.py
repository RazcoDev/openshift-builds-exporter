IMAGESTREAM_TEMPLATE = {
    "apiVersion": "image.openshift.io/v1",
    "kind": "ImageStream",
    "metadata": {
        "annotations": {
            "openshift.io/generated-by": "OpenShiftWebConsole"
        },
        "generation": 1,
        "labels": {
            "app": "build-metric"
        },
        "name": "build-metric",
        "namespace": "",
    },
    "spec": {
        "lookupPolicy": {
            "local": False
        }
    }
}

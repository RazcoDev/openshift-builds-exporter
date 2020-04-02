BUILD_URL = '/apis/build.openshift.io/v1/namespaces/{}/builds/{}'
IMAGE_URL = '/apis/image.openshift.io/v1/images/{}'
INSTANTIATE_URL = '/apis/build.openshift.io/v1/namespaces/{}/buildconfigs/{}/instantiate'
INSTANTIATE_JSON = {
    "kind": "BuildRequest",
    "apiVersion": "build.openshift.io/v1",
    "metadata": {
        "name": "django-ex"
    }
}
BUILDCONFIG_URL = '/apis/build.openshift.io/v1/namespaces/{}/buildconfigs/{}'
IMAGESTREAM_URL = '/apis/image.openshift.io/v1/namespaces/{}/imagestreams/{}'
NODES_URL = '/api/v1/nodes'


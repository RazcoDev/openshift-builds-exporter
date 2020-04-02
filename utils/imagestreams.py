from templates.imagestream import IMAGESTREAM_TEMPLATE


def get_imagestreams_names_list(nodes_names_list: list) -> list:
    return [node_name + '-is' for node_name in nodes_names_list]


def get_formatted_imagestream_template(imagestream_name: str, namespace: str,
                                       imagestream_template: dict = IMAGESTREAM_TEMPLATE):
    imagestream_template['metadata']['name'] = imagestream_name
    imagestream_template['metadata']['namespace'] = namespace
    return imagestream_template

def is_build_finished(build_json: dict) -> bool:
    try:
        return build_json['status']['phase'] in 'Complete'
    except Exception as e:
        print(e)
        return False


def get_finished_build_duration(build_json: dict) -> int:
    # Duration in Golang is on nanoseconds.
    try:
        return build_json['status']['duration'] / 1000000000
    except Exception as e:
        print(e)
        return -1


async def get_builds_json_list(instantiate_results_list: list) -> list:
    builds_json_list =[]
    for result in instantiate_results_list:
        if result is not None and result['kind'] not in 'Status':
            build_json = {'build_name': result['metadata']['name'],
                          'node_name': result['spec']['nodeSelector']['kubernetes.io/hostname'],
                          'buildconfig_name': result['metadata']['labels']['buildconfig'], 'result': None}
            builds_json_list.append(build_json)
    return builds_json_list


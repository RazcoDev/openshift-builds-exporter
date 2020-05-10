from datetime import datetime

async def get_deployments_json_list(deployments_results_list: list) -> list:
    deployments_json_list = []
    for result in deployments_results_list:
        if result is not None and result['kind'] not in 'Status':
            build_json = {'deploy_name': result['metadata']['name'],
                          'node_name': result['spec']['template']['spec']['nodeSelector']['kubernetes.io/hostname'],
                          'result': None}
            deployments_json_list.append(build_json)
    return deployments_json_list


def get_finished_deploy_duration(deployment_json: dict) -> int:
    # Duration in Golang is on nanoseconds.
    try:
        return get_deploy_time_duration(deployment_json['metadata']['annotations']['openshift.io/deployer-pod.created-at'],
                                 deployment_json['metadata']['annotations']['openshift.io/deployer-pod.completed-at'])
    except Exception as e:
        print(e)
        return -1

def get_deploy_time_duration(deploy_time_start: str, deploy_time_completed: str):
    deploy_time_start_formmated = datetime.strptime(deploy_time_start, '%Y-%m-%d %H:%M:%S +0000 UTC')
    deploy_time_completed_formmated = datetime.strptime(deploy_time_completed, '%Y-%m-%d %H:%M:%S +0000 UTC')
    return (deploy_time_completed_formmated- deploy_time_start_formmated).seconds


def is_deployment_finished(deployment_json: dict) -> bool:
    try:
        return deployment_json['metadata']['annotations']['openshift.io/deployment.phase'] in 'Complete'
    except Exception as e:
        print(e)
        return False

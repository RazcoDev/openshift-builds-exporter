def update_build_duration_metric(build_duration_metric, results_json_list: list) -> None:
    [build_duration_metric.metric.set({'node': result['node_name']}, result['result']) for result in results_json_list]


def update_success_rate_metric(success_rate_metric, results_json_list: list) -> None:
    success_rate_metric.metric.set({}, (
            len(results_json_list) - [result['result'] for result in results_json_list].count(-1)) / len(
        results_json_list))

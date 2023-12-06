def state_variable_str_from_ids(
    vehicle_id: int,
    time_step_id: int,
    state_id: int,
) -> str:
    return f"s_{vehicle_id}_{time_step_id}_{state_id}"


def state_slack_variable_str_from_ids(
    vehicle_id: int,
    time_step_id: int,
    state_id: int,
) -> str:
    return f"w_{vehicle_id}_{time_step_id}_{state_id}"


def control_variable_str_from_ids(
    vehicle_id: int,
    time_step_id: int,
    control_id: int,
) -> str:
    return f"u_{vehicle_id}_{time_step_id}_{control_id}"


def control_slack_variable_str_from_ids(
    vehicle_id: int,
    time_step_id: int,
    control_id: int,
) -> str:
    return f"v_{vehicle_id}_{time_step_id}_{control_id}"


def vehicle_collision_binary_slack_variable_str_from_ids(
    vehicle_id: int,
    other_vehicle_id: int,
    time_step_id: int,
    var_id: int,
) -> str:
    assert 0 <= var_id <= 4
    return f"b_{vehicle_id}_{other_vehicle_id}_{time_step_id}_{var_id}"

def obstacle_collision_binary_slack_variable_str_from_ids(
    vehicle_id: int,
    obstacle_id: int,
    time_step_id: int,
    var_id: int,
) -> str:
    assert 0 <= var_id <= 4
    return f"t_{vehicle_id}_{obstacle_id}_{time_step_id}_{var_id}"

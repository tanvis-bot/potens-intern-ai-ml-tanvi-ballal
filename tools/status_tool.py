import random

def check_system_status(service: str):
    """
    Check infrastructure system status.
    """

    statuses = {
        "gpu_cluster": random.choice(["HEALTHY", "DOWN"]),
        "vector_db": random.choice(["HEALTHY", "DEGRADED"]),
        "api_gateway": random.choice(["HEALTHY", "DOWN"])
    }

    return statuses

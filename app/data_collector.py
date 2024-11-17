from datetime import datetime
import random

def collect_data(nodes):
    """Collect alerts, notifications, and logs from the nodes."""
    logs = []
    alerts = []
    for node in nodes:
        event = {
            "node": node,
            "event_type": random.choice(["INFO", "WARNING", "CRITICAL"]),
            "message": f"Sample log from {node}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        logs.append(event)
        if event["event_type"] == "CRITICAL":
            alerts.append(event)
    return logs, alerts

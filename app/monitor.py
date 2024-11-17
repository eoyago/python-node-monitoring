import time
import logging
from data_collector import collect_data
from data_analyzer import analyze_data
from notifications import display_notifications
from logger_config import setup_logging

def main():
    """
    A simplified monitoring flow with hardcoded nodes.
    """
    nodes = ["node1", "node2", "node3"]

    logger = setup_logging()

    while True:
        logs, alerts = collect_data(nodes)
        logger.info(f"Collected {len(logs)} logs and {len(alerts)} alerts.")
        critical_events = analyze_data(alerts)

        if critical_events:
            display_notifications(critical_events)
            logger.warning(f"Critical events detected: {len(critical_events)}")

        time.sleep(10)

def main_loop():
    """
    Main loop to continuously collect data, analyze it, and display notifications.
    """
    nodes = ["node1", "node2", "node3"]
    logging.info("Starting the main loop for Node Monitoring...")

    try:
        while True:
            logs, alerts = collect_data(nodes)
            logging.info(f"Collected {len(logs)} logs and {len(alerts)} alerts.")
            critical_events = analyze_data(alerts)
            if critical_events:
                display_notifications(critical_events)
                logging.warning(f"Critical events detected: {len(critical_events)}")
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Node Monitoring stopped by the user.")
    except Exception as e:
        logging.error(f"An error occurred in the main loop: {e}")

if __name__ == "__main__":
    setup_logging()
    logging.info("Node Monitor application started.")
    main_loop()

def display_notifications(critical_events):
    """Display critical events in the terminal."""
    if critical_events:
        print("\n=== Critical Events ===")
        for event in critical_events:
            print(f"{event['timestamp']} - {event['node']} - {event['message']}")

"""
Phase 1 - OOP: Polymorphism and Python Duck Typing
"""

class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"[EMAIL] Sending message: {message}")

class SMSNotifier:
    def send(self, message: str) -> None:
        print(f"[SMS] Sending message: {message}")

class WebhookNotifier:
    def send(self, message: str) -> None:
        print(f"[WEBHOOK] POST payload: {message}")

def broadcast_alert(notifiers: list, message: str):
    """Polymorphic dispatcher using Duck Typing."""
    for notifier in notifiers:
        notifier.send(message)

channels = [EmailNotifier(), SMSNotifier(), WebhookNotifier()]
broadcast_alert(channels, "Server deployment finished successfully!")

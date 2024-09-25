from app.services.notifier.notifier import NotifierInterface


class ConsoleNotifier(NotifierInterface):
    def notify(self, message: str):
        # Simple console notification
        print(f"Notification: {message}")
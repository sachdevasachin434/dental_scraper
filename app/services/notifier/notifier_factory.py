from app.services.notifier.console_notifier import ConsoleNotifier
import os


class NotifierFactory:
    @staticmethod
    def get_notifier():
        env = os.getenv('ENVIRONMENT', 'local').lower()
        
        if env == 'prod':
            # return EmailStorage()
            pass
        elif env == 'qa':
            # return EmailStorage()
            pass
        else:
            return ConsoleNotifier()
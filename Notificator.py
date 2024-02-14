class Notificator:

    def notify_user(self, user_to_notify: "User", notifier: "User", message: str, log: bool = False, extra_message: str = ""):
        if user_to_notify == notifier:
            return

        user_to_notify.notify(message, log,extra_message)

    def notify_all_followers(self, caller: "User", message: str, log: bool = False):
        for user in caller.followers:
            self.notify_user(user, caller, message, log)

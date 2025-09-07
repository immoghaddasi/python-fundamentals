"""

- Define an interface-like base class Notifier with method send(message).
- Implement EmailNotifier(address) and SMSNotifier(number) that both
implement send.
- Write a function broadcast(notifiers, message) that calls send on any
Notifier passed in. Demonstrate with at least two different notifiers
"""

# Base class acting like an interface
class Notifier:
    def send(self, message):
        # Force subclasses to implement their own send() method
        raise NotImplementedError("Subclasses must implement send()")


# Email notifier subclass
class EmailNotifier(Notifier):
    def __init__(self, address):
        self.address = address

    def send(self, message):
        print(f"Sending email to {self.address}: {message}")


# SMS notifier subclass
class SMSNotifier(Notifier):
    def __init__(self, number):
        self.number = number

    def send(self, message):
        print(f"Sending SMS to {self.number}: {message}")


# Function to broadcast a message to multiple notifiers
def broadcast(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)


email_notifier = EmailNotifier("alice@example.com")
sms_notifier = SMSNotifier("+1234567890")

notifiers = [email_notifier, sms_notifier]

broadcast(notifiers, "Hello! This is a test message.")

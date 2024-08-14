from django.core.management.base import BaseCommand
from message_listener.queue_listener import MessageListener
class Command(BaseCommand):
    help = 'Launches Listener for user_created message : RabbitMQ'
    def handle(self, *args, **options):
        self.stdout.write("Initializing MessageListener...")
        try:
            td = MessageListener()
            td.run()
            self.stdout.write("Started Consumer Thread")
        except Exception as e:
            self.stderr.write(f"Error starting MessageListener: {e}")
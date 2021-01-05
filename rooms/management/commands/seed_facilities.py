from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "Parking and facilities",
            "Free parking on premises",
            "Elevator",
            "Gym",
            "Services",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("facilities created!"))

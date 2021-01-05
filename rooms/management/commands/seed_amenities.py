from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    def handle(self, *args, **options):
        amenities = [
            "Bathroom",
            "Shampoo",
            "Hair dryer",
            "Hot water",
            "Bedroom and laundry",
            "Essentials",
            "Towels, bed sheets, soap, and toilet paper",
            "Iron",
            "Dryer",
            "Hangers",
            "Washer",
            "Entertainment",
            "Cable TV",
            "TV",
            "Heating and cooling",
            "Heating",
            "Air conditioning",
            "Home safety",
            "Unavailable: Security cameras on property",
            "Security cameras on property",
            "Fire extinguisher",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Internet and office",
            "Wifi",
            "Available throughout the listing",
            "Dedicated workspace",
            "Kitchen and dining",
            "Kitchen",
            "Space where guests can cook their own meals",
            "Microwave",
            "Dishes and silverware",
            "Refrigerator",
            "Parking and facilities",
            "Free parking on premises",
            "Elevator",
            "Gym",
            "Services",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))

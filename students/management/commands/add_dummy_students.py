from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = "Adds dummy students to Student database"

    def handle(self, *args, **options):
        # Define the number of students to create
        num_students = 100

        # Create the students
        for i in range(1, num_students + 1):
            first_name = f"Student {i} First Name"
            last_name = f"Student {i} Last Name"
            email = f"student{i}@nci.com"

            student = Student(first_name=first_name, last_name=last_name, email=email)
            student.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully added {num_students} students."))

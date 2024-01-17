from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.db.models import Q
from user.models import User

class Command(BaseCommand):
    help = "Fill the Authentication and Authorization Group in the django admin that all staff can only add and view all models"
    quantity = 0
    def handle(self, *args, **options):
        permissions = Permission.objects.filter(
            Q(codename__startswith="add") | Q(codename__startswith="view")
        )
        staffs = User.objects.filter(is_staff=True, is_superuser=False)
        for staff in staffs:
            for permission in permissions:
                staff.user_permissions.add(permission)
            self.quantity +=1
        if self.quantity > 0:
            self.stdout.write(
                self.style.SUCCESS('Success filled Authentication and Authorization Group in the django admin that all staff can only add and view all models')
            )
            self.stdout.write(
                self.style.SUCCESS('%s staff affected' % self.quantity)
            )
        else:
            CommandError('Oppss.. no staff affected')

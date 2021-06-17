from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    @staticmethod
    def saveContact(name, email, message):
        if (name != "" and email != "" and message != ""):
            contacted = Contact(name=name, email=email, message=message)
            contacted.save()
            return True

        return False
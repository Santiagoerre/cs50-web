from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True)
    clas = models.TextField(blank=True)
    due_date = models.TextField(blank=True)
    link = models.TextField(blank=True, default='default_value')
    done = models.TextField(blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "clas": self.clas,
            "due_date": self.due_date,
            "link": self.link,
            "done": self.done
        }
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from authentication.models import User
import uuid

class Project(models.Model):
    TYPE_CHOICES = (
        ('back-end', 'back-end'),
        ('front-end', 'front-end'),
        ('ios', 'iOS'),
        ('android', 'Android'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

class Issue(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH'),
    )
    BALISE_CHOICES = (
        ('bug', 'BUG'),
        ('feature', 'FEATURE'),
        ('task', 'TASK'),
    )
    STATUS_CHOICES = (
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('finished', 'Finished'),
    )
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='issue')
    assign_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='assigned_issue')
    time_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=2048, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    balise = models.CharField(max_length=10, choices=BALISE_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='to-do')

# uuid is a special ID for comments, we import it.
class Comment(models.Model):
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=2048, blank=True)
    uuid = models.TextField(max_length=2048, blank=True, default=str(uuid.uuid4()))

class Contributor(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)


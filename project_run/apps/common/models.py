from django.db import models

# Create your models here.

class CreatedAtTimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True



class TimeStampedModel(CreatedAtTimeStampedModel):
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
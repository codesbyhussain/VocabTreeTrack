from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Word(MPTTModel):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField()
    sample_sentence = models.TextField()
    
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
    def retdesc(self):
        return self.description
    
    def retsent(self):
        return self.sample_sentence
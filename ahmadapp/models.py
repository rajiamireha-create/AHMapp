from django.db import models
from django.contrib.auth.models import User

class ahmadapptask(models.Model):
    
    manager = models.ForeignKey(User , on_delete = models.CASCADE ,null= True , blank= True, default=None)
    
    task_name = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    class Meta:
        
        ordering = ['id']
    
    
    
    
    def __str__(self):
        return self.task_name + "  " + str(self.done)

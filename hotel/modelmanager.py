from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    #deleted_at = models.BooleanField()

    class Meta:
        abstract = True
        
    # def delete(self):
        # self.deleted_at = True
        # self.save()
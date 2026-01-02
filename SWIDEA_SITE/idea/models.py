from django.db import models
from devtools.models import DevTool

class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ideas/', blank=True, null=True)
    content = models.CharField(max_length=100)
    interest = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    devtool = models.ForeignKey(
        DevTool,
        on_delete=models.CASCADE,
        related_name='ideas',
    )

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='stars')
    created_at = models.DateTimeField(auto_now_add=True)
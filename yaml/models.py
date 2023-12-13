from django.db import models


class Bot(models.Model):
    name = models.CharField(max_length=80, unique=True, help_text='Enter bot name')
    class Meta:
        ordering = ['-name']    
    def __str__(self):
        return self.name


class Intent(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter Intent name')
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-name']
    def __str__(self):
        return self.name


class Response(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter Response name')
    content = models.TextField()
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-name']    
    def __str__(self):
        return self.name


class Story(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter Story name')
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-name']    
    def __str__(self):
        return self.name



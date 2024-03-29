from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True,blank=True,unique=True,db_index=True,editable=False)

    def save(self, *args, **kwargs): #SLUGİFY  
        self.slug = slugify(self.name)
        super().save(*args,**kwargs) 

    def __str__(self) -> str:
        return self.name
    
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True, unique=True, db_index=True)
    categories = models.ManyToManyField(category)


    def __str__(self) -> str:
        return f"{self.title}"
    
    def save(self, *args, **kwargs): #SLUGİFY  
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)  


    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model to get data of home page lead form
class homePageForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # datetime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}" 
    

# model for blogs

# status of blogs
blogs_status = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
)

class blogPost(models.Model):
    
    # title field using charfield constraint with unique constraint
    title = models.CharField(max_length=200, unique=True)
    # slug field auto populated using title with unique constraint
    slug = models.SlugField(max_length=200, unique=True)
    # author field populated using users database
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    # and date time fields automatically populated using system time
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField()
    # content field to store our post
    content = models.TextField()
    # meta description for SEO benefits
    metaDes = models.CharField(max_length=300, default="new post")
    metaTitle = models.CharField(max_length=300, default="new post")
    # status of post
    status = models.IntegerField(choices=blogs_status, default=0)
    image = models.ImageField(default='')
    
    # meta for the class
    # class Meta:
    #     ordering = ['-created_on']
    # used while managing models from terminal
    def __str__(self):
        return self.title
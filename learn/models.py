from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


DIFFCALITY_TYPE = (
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)

SEMESTER_TYPE = (
    ('Semester 5', 'Semester 5'),
    ('Semester 6', 'Semester 6'),
    ('Semester 7', 'Semester 7'),
    ('Semester 8', 'Semester 8'),
    ('Semester 9', 'Semester 9'),
    ('Semester 10', 'Semester 10'),
)


CATEGORY_TYPE = (
    ('SW subjects', 'SW subjects'),
    ('Optional subjects', 'Optional subjects'),
    ('Others', 'Others'),

)

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "learn_Image/%s.%s"%(instance.id , extension)

def Video_upload(instance, filename):
    file , extension = filename.split(".")
    return "learn_Video/%s.%s"%(instance.id , extension)





class learn(models.Model): # table
    title= models.CharField(max_length=100); # reperesent a column
    description = models.TextField(default='write a description')
    urlLearn= models.URLField(max_length = 200)
    published_at = models.DateTimeField(auto_now=True)
    category= models.CharField(max_length=100, choices=CATEGORY_TYPE, default='SW subjects')
    diffcality_type=models.CharField(max_length=15,choices=DIFFCALITY_TYPE,default='easy')
    semester_type = models.CharField(max_length=15, choices=SEMESTER_TYPE, default='Semester 5')
    image= models.ImageField(upload_to=image_upload)
    videofile = models.FileField(upload_to='videos/', null=True)
    tags = TaggableManager()
    author= models.ForeignKey(User, on_delete=models.CASCADE,null=True,default=1)


    def __str__(self):
        return self.title



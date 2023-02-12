from django.db import models

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

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "course/%s.%s"%(instance.id , extension)

class course(models.Model): # table
    title= models.CharField(max_length=100); # reperesent a column
    description = models.TextField(default='write a description')
    credit = models.IntegerField(default=0)
    CRN_num = models.IntegerField(default=0)
    published_at = models.DateTimeField(auto_now=True)
    requirment =models.TextField(default='write a course requirment')
    semester_type = models.CharField(max_length=15, choices=SEMESTER_TYPE, default='Semester 5')
    diffcality_type=models.CharField(max_length=15,choices=DIFFCALITY_TYPE,default='easy')
    facality_members = models.TextField(default='write a facality member')
    image= models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.title








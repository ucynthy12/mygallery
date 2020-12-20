from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name= models.CharField(max_length=50)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name
        
class Image(models.Model):
    gallery_image = models.ImageField(upload_to = 'album/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls,id,name):
        cls.objects.filter(id=id).update(name=name)

    @classmethod
    def get_image_by_id(cls,id):

        image=cls.objects.filter(id=id).all()
        return image



    @classmethod
    def search_image(cls,category):
        album = cls.objects.filter(category__name__icontains=category)
        return album

    @classmethod
    def filter_by_location(cls,location):
        image_loc = Image.objects.filter(location__name=location).all()
        return image_loc

    def __str__(self):

        return self.name

    class Meta:
        ordering = ['pub_date']

    
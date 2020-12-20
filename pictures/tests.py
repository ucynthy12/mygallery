from django.test import TestCase
from .models import Category,Location,Image
# Create your tests here.

class ImageTestClass(TestCase):
    
    def setUp(self):
        self.category= Category(name='nature')
        self.category.save_category()

        self.location = Location(name='desert')
        self.location.save_location()

        self.new_image= Image(name='flower',description='yellow flower',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    
    def test_save_method(self):
        self.new_image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.new_image.save_image()
       
        self.new_image.delete_image()
        images= Image.objects.all()
        self.assertTrue(len(images)== 0)
    
    def test_update_method(self):
        self.new_image.save_image()

        self.new_image.update_image(id=1,name='blue flower')
        images = Image.objects.all()
        self.assertTrue(len(images)==1)

    def test_get_image_by_id(self):
        self.new_image.save_image()
        find_image = self.new_image.get_image_by_id(self.new_image.id)
        image = Image.objects.filter(id=1)
        self.assertTrue(find_image,image)

    def test_get_image_by_location(self):
        self.new_image.save_image()
        find_image = self.new_image.filter_by_location(location='desert')
        self.assertTrue(len(find_image)==1)

    def test_search_method_by_category(self):
        category='nature'
        self.new_image.save_image()
        find_image = self.new_image.search_image(category)
        self.assertTrue(len(find_image) >=1)


    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
class LocationTestClass(TestCase):

    def setUp(self):
        self.location= Location(name='desert')
        self.location.save_location()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category= Category(name='nature')
        self.category.save_category()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    



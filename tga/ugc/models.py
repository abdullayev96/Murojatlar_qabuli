from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    lang_id = models.IntegerField()
    chat_id = models.IntegerField()

    def __str__(self):
        #return f'{self.first_name} {self.last_name} {str(self.chat_id)}'
        return str(self.chat_id)

    class Meta:
        db_table = 'user'
        managed = False
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

# class Category(models.Model):
#     name_uz = models.CharField(max_length=150)
#     name_ru = models.CharField(max_length=150)
#     name_en = models.CharField(max_length=150, null=True, blank=True)
#     parent = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return f'{self.name_uz}'
#
#     class Meta:
#         db_table = 'category'
#         managed = False
#         verbose_name = 'Kategoriya'
#         verbose_name_plural = 'Kategoriyalar'


# class Product(models.Model):
#     name_uz = models.CharField(max_length=150)
#     name_ru = models.CharField(max_length=150)
#     name_en = models.CharField(max_length=150, null=True, blank=True)
#     category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
#     description_uz = models.TextField(null=False, blank=False)
#     description_ru = models.TextField(null=False, blank=False)
#     description_en = models.TextField(null=True, blank=True)
#     price = models.IntegerField(null=False, blank=False)
#     image = models.ImageField(upload_to='images/')
#
#     def __str__(self):
#         return f'{self.name_uz}'
#
#     class Meta:
#         db_table = 'product'
#         managed = False
#         verbose_name = "O'quv kurs"
#         verbose_name_plural = "O'quv kurslari"
#
#
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     status = models.IntegerField()
#     payment_type = models.CharField(max_length=50)
#     longitude = models.FloatField()
#     latitude = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class OrderProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     amount = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    text_uz = models.TextField()
    text_en = models.TextField(null=True, blank=True)
    text_ru = models.TextField()

    def __str__(self):
        return f'{self.text_uz}'

    class Meta:
        db_table = 'about_us'
        managed = False
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'

class Comment(models.Model):
    user_id = models.IntegerField()
    comment_text = models.TextField()
    username = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='users/', verbose_name="rasmlar")
    # file = models.FileField(upload_to='files/', verbose_name='Fayllar')


    def __str__(self):
        return f'{self.username}'

    class Meta:
        db_table = 'comment'
        managed = False
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"

class New(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    heading_uz = models.CharField(max_length=500)
    heading_en = models.CharField(max_length=500, null=True, blank=True)
    heading_ru = models.CharField(max_length=500)

    text_uz = models.TextField()
    text_en = models.TextField(null=True, blank=True)
    text_ru = models.TextField()


    def __str__(self):
        return f'{self.heading_uz}'

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


class User_test(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()
    username = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.message} ||{self.username}'"


    class Meta:
        verbose_name = "Taklif"
        verbose_name_plural = "Takliflar"

class Murojat(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()
    username = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.message} ||{self.username}'"


    class Meta:
        verbose_name = "Shikoyat va Muammo"
        verbose_name_plural = "Shikoyat va Muammolar"


class Information(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()
    username = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.message} ||{self.username}'"

    class Meta:
        verbose_name = "Malumot"
        verbose_name_plural = "Malumotlar"

# class Test_result(models.Model):
#     id_number  = models.PositiveIntegerField()
#     #image  = models.ImageField(upload_to='images/', null=True, blank=True)
#     file  = models.FileField(upload_to='files/', verbose_name="file nomi")
#     posted_at = models.DateTimeField(auto_now_add=True)
#     heading_uz = models.CharField(max_length=500)
#     heading_ru = models.CharField(max_length=500)
#     heading_en = models.CharField(max_length=500, null=True, blank=True)
#     text_uz = models.TextField()
#     text_ru = models.TextField()
#     text_en = models.TextField(null=True, blank=True)
#
#
#     def __str__(self):
#         return f'{self.heading_uz}'
#
#     class Meta:
#         verbose_name  = "Test_natija"
#         verbose_name_plural = "Test_natijalari"
#










from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country =models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    sex = models.BooleanField(choices=((0, '男'), (1, '女')))
    email = models.EmailField()
    address = models.CharField(max_length=20)
    birthday = models.DateField()
    author = models.OneToOneField(Author)

    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

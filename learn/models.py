from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SexQuerySet(models.QuerySet):
    def male_list(self):
        return self.filter(authordetail__sex=True)


class NewSexManager(models.Manager):
    def get_queryset(self):
        return SexQuerySet(self.model, using=self._db)

    def male_list(self):
        return self.get_queryset().male_list()


class MaleAuthor(models.Manager):
    def get_queryset(self):
        return super(MaleAuthor, self).get_queryset().filter(authordetail__sex=True)

    # def reverse(self):
    #     return self.filter(authordetail__sex=False)


class SexManager(models.Manager):
    def reverse(self):
        return self.filter(authordetail__sex=False)


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    new_sex_manager = SexQuerySet.as_manager()
    sex_manager = SexManager()
    male_authors = MaleAuthor()


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

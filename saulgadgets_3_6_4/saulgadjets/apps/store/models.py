from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    #To specify how the plural form should be
    class Meta:
        verbose_name_plural = "Categories"
        # The comer is added because it is a tuple
        ordering = ("ordering",)

    def __str__(self):

        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #minus is used in order to make the ordering in descending order
        ordering = ("-date_added",)

    def __str__(self):

        return self.title

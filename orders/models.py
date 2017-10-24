from django.db import models


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(TimeStamp):
    job_number = models.CharField(max_length=7)
    company = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    class Meta:
        ordering = ['job_number']

    def __str__(self):
        return self.job_number


class Test(TimeStamp):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50)
    air_flow_rate = models.CharField(max_length=50)
    filter_description = models.CharField(max_length=50)

    def __str__(self):
        return self.test_type



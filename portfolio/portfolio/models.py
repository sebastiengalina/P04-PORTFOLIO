# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy as reverse

# Third Party
from sorl.thumbnail import ImageField


## ----------------------------------------------------------------------------
## PORTFOLIO PROJECT
## ----------------------------------------------------------------------------
class Project(models.Model):
    # Identifying information
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    ptype = models.CharField(verbose_name=_("Project type"), max_length=64)

    # Logistic information
    client = models.CharField(max_length=64)
    date = models.DateField(verbose_name=_("End date of project"))

    # Navigation information
    logo = ImageField(upload_to="media/portfolio/projects/logos", blank=True, null=True)
    image = ImageField(upload_to="media/portfolio/projects/images", blank=True, null=True)
    short = models.TextField(verbose_name=_("Short description"))
    readmore = models.CharField(verbose_name=_("Read more link text"), max_length=64)
    tags = models.ManyToManyField("Tag", blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project", args=[self.slug])

    class Meta:
        ordering = ("-date",)


## ----------------------------------------------------------------------------
## PORTFOLIO PROJECT BLOCK
## Used to add structured information blocks to project detail page
## ----------------------------------------------------------------------------
class ProjectBlock(models.Model):
    project = models.ForeignKey("Project", related_name="blocks")
    heading = models.CharField(max_length=255, blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = ImageField(upload_to="media/portfolio/projects/images", blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=10)

    def __unicode__(self):
        return self.heading

    class Meta:
        ordering = ("order",)


## ----------------------------------------------------------------------------
## CATEGORY TAGS
## ----------------------------------------------------------------------------
class Tag(models.Model):
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag", args=[self.name.lower()])

from django.utils.text import slugify
from django_lifecycle import AFTER_CREATE
from django_lifecycle import AFTER_UPDATE
from django_lifecycle import BEFORE_SAVE
from django_lifecycle import hook
from django_lifecycle import LifecycleModel


class SlugMixin(LifecycleModel):
    @hook(AFTER_UPDATE, when="name", has_changed=True)
    @hook(AFTER_CREATE)
    def set_slug(self):
        self.slug = slugify(self.name)  # type: ignore

    class Meta:
        abstract = True

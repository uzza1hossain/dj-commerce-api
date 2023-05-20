from django.utils.text import slugify
from django_lifecycle import BEFORE_CREATE
from django_lifecycle import BEFORE_UPDATE
from django_lifecycle import hook
from django_lifecycle import LifecycleModelMixin


class SlugMixin(LifecycleModelMixin):
    @hook(BEFORE_UPDATE, when="name", has_changed=True)
    @hook(BEFORE_CREATE)
    def set_slug(self):
        self.slug = slugify(self.name)  # type: ignore

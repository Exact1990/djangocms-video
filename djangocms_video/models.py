import os

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path on django CMS 3.0.4+ for information
        """
        return instance.get_media_path(filename)
from cms.utils.compat.dj import python_2_unicode_compatible

from . import settings


@python_2_unicode_compatible
class Video(CMSPlugin):
    # player settings
    movie = models.FileField(
        _('movie file'), upload_to=get_plugin_media_path,
        help_text=_('use .flv file or h264 encoded video file'), blank=True,
        null=True)

    image = models.ImageField(
        _('image'), upload_to=get_plugin_media_path,
        help_text=_('preview image file'), null=True, blank=True)
    
    width = models.PositiveSmallIntegerField(_('width'))

    height = models.PositiveSmallIntegerField(_('height'))
    
    auto_play = models.BooleanField(
        _('auto play'), default=settings.VIDEO_AUTOPLAY)

    loop = models.BooleanField(_('loop'), default=settings.VIDEO_LOOP)

    def __str__(self):
        if self.movie:
            name = self.movie.path
        else:
            name = ''
        return u"%s" % os.path.basename(name)

    def get_height(self):
        return "%s" % self.height
    
    def get_width(self):
        return "%s" % self.width
    
    def get_movie(self):
        if self.movie:
            return self.movie.url


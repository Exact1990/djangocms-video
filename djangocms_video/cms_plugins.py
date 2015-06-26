from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import settings
from .forms import VideoForm
from .models import Video


class VideoPlugin(CMSPluginBase):
    model = Video
    name = _("Video")
    form = VideoForm
    text_enabled = True
    
    render_template = "cms/plugins/video.html"
    
    general_fields = [
        'movie',
        'image',
        ('width', 'height'),
        'auto_play',
        'loop',
    ]
    
    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
    ]
        
    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
    
plugin_pool.register_plugin(VideoPlugin)
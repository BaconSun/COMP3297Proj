from django.conf.urls import include, url
from . import module_views

urlpatterns = [
    url(r'^(?P<identity>Participant|Instructor)/(?P<username>[A-Za-z\d_\s]+)', module_views.view_module, name='view_module'),
    url(r'^create_text_component/(?P<username>[A-Za-z\d_\s]+)', module_views.create_text_component, name='create_text_component'),
    url(r'^create_image_component/(?P<username>[A-Za-z\d_\s]+)', module_views.create_image_component, name='create_image_component'),
    url(r'^create_file_component/(?P<username>[A-Za-z\d_\s]+)', module_views.create_file_component, name='create_file_component'),
    url(r'^(?P<component>[A-Za-z\d_\s]+)/', include('sdp.component_urls')),
]

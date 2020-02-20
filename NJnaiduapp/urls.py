from django.contrib import admin
from django.urls import path
from NJnaiduapp import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('chairman_create', views.chairman_create, name='chairman_create'),
    path('chairman_update', views.chairman_update, name='chairman_update'),
    path('', views.index, name='index'),
    path('our_hospital', views.our_hospital, name='our_hospital'),
    path('chairman', views.chairman, name='chairman'),
    path('our_team', views.our_team, name='our_team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('arthoplasty', views.arthoplasty, name='arthoplasty'),
    path('htp_replacement', views.htp_replacement, name='htp_replacement'),
    path('knee_replacement', views.knee_replacement, name='knee_replacement'),
    path('arthoscopy', views.arthoscopy, name='arthoscopy'),
    path('orthopaedics', views.orthopaedics, name='orthopaedics'),
    path('arthritis', views.arthritis, name='arthritis'),
    path('bonetumours', views.bonetumours, name='bonetumours'),
    path('illizarov', views.illizarov, name='illizarov'),
    path('orthosuv', views.orthosuv, name='orthosuv'),
    path('osteoporosis', views.osteoporosis, name='osteoporosis'),
    path('paediatric', views.paediatric, name='paediatric'),
    path('trauma', views.trauma, name='trauma'),
    path('spine', views.spine, name='spine'),
    path('radiology', views.radiology, name='radiology'),
    path('painmanagement', views.painmanagement, name='painmanagement'),
    path('physiotheraphy', views.physiotheraphy, name='physiotheraphy'),
    path('success_stories', views.success_stories, name='success_stories'),
    path('empanelment', views.empanelment, name='empanelment'),
    path('ehs_ntr', views.ehs_ntr, name='ehs_ntr'),
    path('acl_rehab', views.acl_rehab, name='acl_rehab'),
    path('packages', views.packages, name='packages'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
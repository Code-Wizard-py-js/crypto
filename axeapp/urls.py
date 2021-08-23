from django.contrib import admin
from django.urls import path,include
from. import views
#Sivan,Forest,Arctic,Mystic,Genesis
urlpatterns = [
   path(r'api/land/sivannah',views.SivnaView),
   path(r'api/land/Forest',views.ForestView),
   path(r'api/land/Arctic',views.ArcticView),
   path(r'api/land/Mystic',views.MysticView),
   path(r'api/land/Genesis',views.GenesisView),
   
]



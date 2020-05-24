from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  
    path('signup/', views.UserProfileListviews.as_view(), name='UserProfileListviews'),
    path('coronatracker/',views.CoronaTrackerListviews.as_view(),name='CoronaTrackerListviews'),
    path('Login_generate_otp/',views.Login_generate_otpviews.as_view(),name='Login_generate_otpviews'),
    path('Login_verify_otp/',views.Login_verify_otpviews.as_view(),name='Login_verify_otpviews'),
    path('country/',views.Countryviews.as_view(),name='Countryviews'),
    path('globaldata/',views.GlobalCoronatracker_Recordviews.as_view(),name='GlobalCoronatracker_Recordviews'),
    path('paintsvilla/',views.Paintsvillaviews.as_view(),name='Paintsvillaviews'),
    
    
    
]

if True:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
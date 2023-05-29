from django.urls import path

# from .views import uptest,thakyou,sample,single,singleview,review,create,favourate

from .views import single,favourate,shiva
urlpatterns = [
    # path('', uptest.as_view()),
    # path('thankyou/',thakyou.as_view(),name="thank"),
    # path('datail/',sample.as_view(),name="sample"),
    path('view/favourate',favourate.as_view(),name="sound"),
    path('result/<int:id>/',single.as_view(),name="result"),
    path('shiva/',shiva.as_view(),name="kumar"),
    
    
    # path('view/<int:pk>/',singleview.as_view()),
    # path('form/',review.as_view()),
    # path('create/',create.as_view())
]
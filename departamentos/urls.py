from django.urls import path
from .views import *

app_name='departamentos'

urlpatterns = [
    path('', DepartamentosHomeView.as_view(), name='index'),
    path('crear',crear.as_view(),name="crear"),
    # path('eliminar/<int:id>', eliminar),
    # path('editar/<int:id>',editar),

]
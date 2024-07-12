from django.urls import path
from .views import (
    add_to_cart, almacenero_view, finalize_purchase, remove_from_cart, responsable_almacen_view, analista_inventario_view, gerente_view, 
    gerente_inventario_view, register, profile_view, dashboard, generate_report, 
    registrar_movimiento_inventario, compra_view
)

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('almacenero/', almacenero_view, name='almacenero'),
    path('responsable/', responsable_almacen_view, name='responsable_almacen'),
    path('analista/', analista_inventario_view, name='analista_inventario'),
    path('gerente/', gerente_view, name='gerente'),
    path('gerente_inventario/', gerente_inventario_view, name='gerente_inventario'),
    path('generate_report/', generate_report, name='generate_report'),
    path('registrar_movimiento/', registrar_movimiento_inventario, name='registrar_movimiento'),
    path('compra/', compra_view, name='compra'),
    path('add_to_cart/<int:material_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:material_id>/', remove_from_cart, name='remove_from_cart'),
    path('finalize_purchase/', finalize_purchase, name='finalize_purchase'),
]

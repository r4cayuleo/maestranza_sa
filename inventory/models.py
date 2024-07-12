from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    max_capacity = models.IntegerField(default=100)  # Capacidad máxima

    class Meta:
        permissions = [
            ("can_manage_storage", "Can manage storage"),
            ("can_access_almacenero", "Can access almacenero view"),
            ("can_access_responsable_almacen", "Can access responsable almacen view"),
            ("can_access_analista_inventario", "Can access analista inventario view"),
            ("can_access_gerente", "Can access gerente view"),
            ("can_access_gerente_inventario", "Can access gerente inventario view"),
        ]

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)
    description = models.TextField()
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    condition = models.CharField(max_length=50, choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado'), ('Reparado', 'Reparado')], default='Nuevo')
    nivel_critico = models.IntegerField(default=0)
    etiquetas = models.CharField(max_length=200, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    numero_serie = models.CharField(max_length=100, null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class StorageCapacity(models.Model):
    limit = models.IntegerField(default=1000)  # Capacidad total del almacén

    def __str__(self):
        return f"Capacity Limit: {self.limit}"

class Alert(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alert at {self.location.name} by {self.created_by.username}"

class MovimientoInventario(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=50)  # Entrada, Salida, etc.
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.CharField(max_length=100, null=True, blank=True)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.material.name} ({self.quantity})"
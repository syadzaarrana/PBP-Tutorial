from dataclasses import field
from django.db import models
from django import forms

# Create your models here.
class BarangWishlist(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()

class AddWishlist(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang', 'harga_barang', 'deskripsi']

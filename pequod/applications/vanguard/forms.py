from django import forms
from .models import products, suppliers, product_categories, product_status, brands, suppliers_status, suppliers_levels


class formUpdateproduct(forms.ModelForm):

    class Meta:
        model = products
        fields = ['part_number', 'name', 'title', 'price', 
                  'description', 'brand', 'model', 'quantity', 
                  'supplier', 'category', 'google_title', 'specs', 
                  'sku', 'product_status', 'main_image', 'slug', 
                  'weight', 'height', 'width', 'deep', ]

        widgets = {
            'email': forms.TextInput(
                attrs= {

                }
            )
        }



class formNewProduct(forms.ModelForm):

    class Meta:
        model = products
        fields = ('__all__')



class formUpdateSupplier(forms.ModelForm):

    class Meta:
        model = suppliers
        fields = ['supplier_name', 'supplier_description', 'supplier_brand', 'supplier_level', 
                  'supplier_status', 'specialty',]
        


class formNewSupplier(forms.ModelForm):

    class Meta:
        model = suppliers
        fields = ('__all__')


class formUpdateProductCategory(forms.ModelForm):

    class Meta:
        model = product_categories
        fields = ('__all__')


class formNewProductCategory(forms.ModelForm):

    class Meta:
        model = product_categories
        fields = ('__all__')


class formUpdateProductStatus(forms.ModelForm):

    class Meta:
        model = product_status
        fields = ('__all__')


class formNewProductStatus(forms.ModelForm):

    class Meta:
        model = product_status
        fields = ('__all__')


class formUpdateBrand(forms.ModelForm):

    class Meta:
        model = brands
        fields = ('__all__')


class formNewBrand(forms.ModelForm):

    class Meta:
        model = brands
        fields = ('__all__')


class formUpdateSupplierStatus(forms.ModelForm):

    class Meta:
        model = suppliers_status
        fields = ('__all__')


class formNewSupplierStatus(forms.ModelForm):

    class Meta:
        model = suppliers_status
        fields = ('__all__')


class formUpdateSupplierLevel(forms.ModelForm):

    class Meta:
        model = suppliers_levels
        fields = ('__all__')


class formNewSupplierLevel(forms.ModelForm):

    class Meta:
        model = suppliers_levels
        fields = ('__all__')

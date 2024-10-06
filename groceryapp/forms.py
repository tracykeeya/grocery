from django import forms
from django.core.exceptions import ValidationError
from .models import Sale, CreditSale, Stocks




class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price is None or unit_price < 0:
            raise ValidationError("Unit price must be a positive number.")
        return unit_price   

class CreditSaleForm(forms.ModelForm):
    class Meta:
        model = CreditSale
        fields = ['buyer_name', 'national_id', 'location', 'contacts', 'amount_due', 'sales_agent_name', 'due_date', 'produce_name', 'produce_type', 'tonnage', 'dispatch_date']


class StocksForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = [
            'item_name', 'stock_types', 'stock_date', 'total_quantity', 
            'stock_cost', 'stock_dealer_name', 'stock_branch_name', 'stock_contact', 'unit_price'
        ]

    # Custom validation for 'item_name' (at least 2 characters)
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if len(item_name) < 2:
            raise ValidationError('Item name must be at least 2 characters long.')
        return item_name

    # Custom validation for 'total_quantity' (numeric and at least 1)
    def clean_total_quantity(self):
        total_quantity = self.cleaned_data.get('total_quantity')
        if total_quantity <= 0:
            raise ValidationError('Total quantity must be greater than 0.')
        return total_quantity

    # Custom validation for 'stock_cost' (numeric, must be at least 5 characters)
    def clean_stock_cost(self):
        stock_cost = self.cleaned_data.get('stock_cost')
        if stock_cost < 10000:  # Assuming you want a minimum cost of 10,000 UGX
            raise ValidationError('Stock cost must be at least 10,000 UGX.')
        return stock_cost

    # Custom validation for 'stock_contact' (valid phone number format)
    def clean_stock_contact(self):
        stock_contact = self.cleaned_data.get('stock_contact')
        if len(stock_contact) != 10 or not stock_contact.isdigit():
            raise ValidationError('Enter a valid 10-digit phone number.')
        return stock_contact

    # Custom validation for 'unit_price' (numeric and greater than 0)
    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price <= 0:
            raise ValidationError('Unit price must be greater than 0.')
        return unit_price

    # You can add more custom validation for other fields as needed.



class   AddForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['total_quantity'] 



"""class StocksForm(forms.ModelForm):

    class Meta:
        model = Stocks
        fields = ['item_name', 'stock_types', 'stock_date', 'total_quantity', 'stock_cost', 'stock_dealer_name', 'stock_branch_name', 'stock_contact', 'unit_price']

    # Custom validation for item_name
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')

        # Check if item_name is empty
        if not item_name:
            raise ValidationError('Item name is required.')

        # Check if item_name is at least 2 characters long
        if len(item_name) < 2:
            raise ValidationError('Item name must be at least 2 characters long.')

        return item_name
              

"""


class StocksForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = [
            'item_name', 'stock_types', 'stock_date', 'total_quantity', 
            'stock_cost', 'stock_dealer_name', 'stock_branch_name', 'stock_contact', 'unit_price'
        ]

    # Custom validation for 'item_name' (at least 2 characters)
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise ValidationError('Item name is required.')
        if len(item_name) < 2:
            raise ValidationError('Item name must be at least 2 characters long.')
        return item_name

    # Custom validation for 'stock_types' (ensure it's not empty)
    def clean_stock_types(self):
        stock_types = self.cleaned_data.get('stock_types')
        if not stock_types:
            raise ValidationError('Stock type is required.')
        return stock_types

    # Custom validation for 'stock_date' (ensure date is provided)
    def clean_stock_date(self):
        stock_date = self.cleaned_data.get('stock_date')
        if not stock_date:
            raise ValidationError('Stock date is required.')
        return stock_date

    # Custom validation for 'total_quantity' (numeric and greater than 0)
    def clean_total_quantity(self):
        total_quantity = self.cleaned_data.get('total_quantity')
        if total_quantity is None or total_quantity <= 0:
            raise ValidationError('Total quantity must be greater than 0.')
        return total_quantity

    # Custom validation for 'stock_cost' (numeric and at least 5 characters)
    def clean_stock_cost(self):
        stock_cost = self.cleaned_data.get('stock_cost')
        if stock_cost is None or stock_cost < 10000:  # Minimum cost of 10,000 UGX
            raise ValidationError('Stock cost must be at least 10,000 UGX.')
        return stock_cost

    # Custom validation for 'stock_dealer_name' (at least 2 characters)
    def clean_stock_dealer_name(self):
        stock_dealer_name = self.cleaned_data.get('stock_dealer_name')
        if not stock_dealer_name:
            raise ValidationError('Dealer name is required.')
        if len(stock_dealer_name) < 2:
            raise ValidationError('Dealer name must be at least 2 characters long.')
        return stock_dealer_name

    # Custom validation for 'stock_branch_name' (ensure it's not empty)
    def clean_stock_branch_name(self):
        stock_branch_name = self.cleaned_data.get('stock_branch_name')
        if not stock_branch_name:
            raise ValidationError('Branch name is required.')
        return stock_branch_name

    # Custom validation for 'stock_contact' (valid phone number format)
    def clean_stock_contact(self):
        stock_contact = self.cleaned_data.get('stock_contact')
        if not stock_contact or len(stock_contact) != 10 or not stock_contact.isdigit():
            raise ValidationError('Enter a valid 10-digit phone number.')
        return stock_contact

    # Custom validation for 'unit_price' (numeric and greater than 0)
    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price is None or unit_price <= 0:
            raise ValidationError('Unit price must be greater than 0.')
        return unit_price


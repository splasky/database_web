from django import forms


class employee_create_form(forms.form):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=True)
	phonenumber = models.CharField(max_length=200)
	EMP_gender = ((M, 'male'), (F, 'female'))
    gender = models.CharField(max_length=6, choices=EMP_gender)
	birthday = models.DateField()

	



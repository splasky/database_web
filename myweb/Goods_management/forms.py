from django import forms


class MasterForm(forms.Form):
	Manufacturer = forms.CharField(max_length=100)
	staff = forms.CharField(max_length=10)
	contact_person = forms.CharField('聯絡人', max_length=16)
    contact_person_phone=forms.IntegerField('聯絡電話',)
	remarks=forms.TextField('備註',max_length=200,blank=True, null=True)
	address = forms.CharField('地址', max_length=200)

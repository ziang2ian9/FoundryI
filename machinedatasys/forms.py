from django import forms


class AddedReport(forms.Form):
    problem = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "ปํญหาที่พบเจอ"
        })
    )
    fix = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "วีธีแก้ไข"
        })
    )

class Add_machine(forms.Form):
	name = forms.CharField(
		max_length=60,
		widget=forms.TextInput(attrs={
		"class": "form-control",
		"placeholder" : "ชื่อเครื่อง"
		})
	)
	Description = forms.CharField(
		max_length=60,
		widget=forms.TextInput(attrs={
		"class": "form-control",
		"placeholder" : "คำอธิบายเครื่อง"
		})
	)

class Add_image(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()
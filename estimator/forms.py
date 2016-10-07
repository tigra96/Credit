from django import forms
from .models import Estimate
from .models import LogIn
from .models import client_info
from .models import client_history
from .models import client_job
from .models import surname
import datetime

my_default_errors = {
    'required': 'Заполните это поле',
    'invalid': 'Неверные данные'
}

class SurnameForm(forms.ModelForm):
	Second_Name = forms.CharField(label=u'Поиск по фамилии', max_length=30, error_messages=my_default_errors, required=False,)
	class Meta:
		model = surname
		fields = ('Second_Name',)


class RequestForm(forms.ModelForm):
	CHOICES = (('01','Январь'),('02', 'Февраль'),('03', 'Март'),('04', 'Апрель'),('05', 'Май'),('06', 'Июнь'),('07', 'Июль'),('08', 'Август'),('09', 'Сентябрь'),('10', 'Октябрь'),('11', 'Ноябрь'),('12', 'Декабрь'))
	Second_Name = forms.CharField(label=u'Фамилия', max_length=30, error_messages=my_default_errors)
	Name = forms.CharField(label=u'Имя', max_length=30, error_messages=my_default_errors)
	Last_Name = forms.CharField(label=u'Отчество', max_length=30, error_messages=my_default_errors)
	birth_day = forms.DateField(required=False, label=u'Дата рождения', initial=datetime.date.today, error_messages=my_default_errors, help_text=' гггг-мм-дд')
	passport = forms.IntegerField(label=u'Номер паспорта', error_messages=my_default_errors)
	Amount = forms.IntegerField(label=u'Сумма кредита', error_messages=my_default_errors)
	Salary = forms.IntegerField(label=u'Зарплата', error_messages=my_default_errors)
	Work_Experience = forms.IntegerField(label=u'Опыт работы', error_messages=my_default_errors, help_text='в месяцах')
	Repayment_Period = forms.IntegerField(label=u'Срок выплаты кредита', error_messages=my_default_errors, help_text='в месяцах')

	class Meta:
		model = Estimate
		fields = ('Second_Name', 'Name', 'Last_Name', 'birth_day',  'Amount', 'Salary', 'Work_Experience', 'Repayment_Period',)
 
class LogInForm(forms.ModelForm):
	Username = forms.CharField(label=u'Логин', max_length=20, error_messages=my_default_errors)
	Password = forms.CharField(label=u'Пароль', max_length=20, error_messages=my_default_errors)
	
	class Meta:
		model = LogIn
		fields = ('Username', 'Password',)

		
class ClientsInfoForm(forms.ModelForm):
	second_name = forms.CharField(label=u'Фамилия',max_length=20, error_messages=my_default_errors)
	first_name = forms.CharField(label=u'Имя', max_length=20, error_messages=my_default_errors)
	third_name = forms.CharField(label=u'Отчество',max_length=20, error_messages=my_default_errors)
	birth = forms.DateField(label=u'Дата рождения', initial=datetime.date.today, help_text=' гггг-мм-дд', error_messages=my_default_errors)
	passport = forms.IntegerField(label=u'Номер паспорта', error_messages=my_default_errors)
	email = forms.EmailField(required=False)
	
	class Meta:	
		model = client_info
		fields = ('second_name', 'first_name', 'third_name',)
		
class ClientsHistForm(forms.ModelForm):
	CHOICES = (('Выдан','Выдан'),('Погашен', 'Погашен'),('Задержен', 'Задержен'))
	passport = forms.IntegerField(label=u'Номер паспорта', error_messages=my_default_errors)
	start_credit = forms.DateField(label=u'Дата выдачи кредита', initial=datetime.date.today, help_text=' гггг-мм-дд', error_messages=my_default_errors)
	finish_credit = forms.DateField(label=u'Дата погашения кредита', initial=datetime.date.today, help_text=' гггг-мм-дд', error_messages=my_default_errors)
	amount = forms.IntegerField(label=u'Сумма кредита', error_messages=my_default_errors)	
	number_of_delays = forms.IntegerField(label=u'Количество задержек', error_messages=my_default_errors)	
	status = forms.ChoiceField(widget = forms.Select(), label=u'Статус', error_messages=my_default_errors, choices=CHOICES)
	
	class Meta:	
		model = client_history
		fields = ('passport', 'start_credit', 'finish_credit',)		
		
		
class ClientsJobForm(forms.ModelForm):
	work_place = forms.CharField(label=u'Место работы',max_length=20, error_messages=my_default_errors)
	salary = forms.IntegerField(label=u'Зарплата', error_messages=my_default_errors)
	experience = forms.IntegerField(label=u'Опыт работы', error_messages=my_default_errors)
	
	class Meta:	
		model = client_job
		fields = ('work_place', 'salary', 'experience',)
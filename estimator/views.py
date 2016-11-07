from django.shortcuts import render
import sqlite3 as lite
import sys
from .forms import RequestForm, LogInForm, ClientsInfoForm, ClientsHistForm, ClientsJobForm, SurnameForm
from django.shortcuts import render, get_object_or_404
from .models import Estimate, client_info, client_history, client_job, LogIn
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ValidationError

con = lite.connect('db.sqlite3', check_same_thread=False)
activation = 0
num = 0
num_form = 0
num_sel = 0
surname = ""


# Create your views here.

def estimator_list(request):
	return render(request, 'estimator/estimator_list.html', {})
	
def post_new(request):

	form = RequestForm(request.POST)
	text = ""
	
	if request.method == "POST":
		if form.is_valid():			
			Second_Name = form.cleaned_data['Second_Name']		
			Name = form.cleaned_data['Name']
			Last_Name = form.cleaned_data['Last_Name']	
			birth = form.cleaned_data['birth_day']	
			passport = form.cleaned_data['passport']	
			Amount = form.cleaned_data['Amount']
			Salary = form.cleaned_data['Salary']
			Work_Experience = form.cleaned_data['Work_Experience']
			Repayment_Period = form.cleaned_data['Repayment_Period']
			Age = 2016 - int(str(birth).split("-")[0])
	
			
			with con:
				cur = con.cursor()    
				cur.execute("Select Id FROM BCH_Personal_info WHERE passport=?", [passport])         
				rows = cur.fetchall()

			if len(rows) == 0:
				text = "Сожалеем, но бюро кредитных историй не смогло предоставить информацию о вашей кредитной истории!"	
			else:
				with con:
					cur = con.cursor()    
					cur.execute("Select * FROM BCH_Credit_info WHERE id_person=?", [rows[0][0]])         
					rows = cur.fetchall()
				current = 0
				delays = 0
				for i in range(len(rows)):
					if int(rows[i][3].split("-")[0]) > 2016:
						current += 1
					delays += int(rows[i][5])	
				if (1):
					text = "Поздравляем, у вас хорошие шансы на получение кредита!"				
				else:
					text = "Сожалеем, но вас маловато шансов на получение кредита!"		
			form = RequestForm()

	else:
		form = RequestForm()
	return render(request, 'estimator/post_edit.html', {'form': form, 'text': text})
	
def estimate_result(request):
       return render(request, 'estimator/estimate_result.html')
	   
def estimate_bad_result(request):
       return render(request, 'estimator/estimate_bad_result.html')
	   
def estimate_credit_history(request):
       return render(request, 'estimator/credit_history.html')
	   
def estimate_model_info(request):
       return render(request, 'estimator/model_info.html')
	 
def estimate_bad_answer(request):
       return render(request, 'estimator/estimate_bad_answer.html')	 
	   
def estimate_login(request):
	if activation:
		return redirect('estimator.views.estimate_admin')
	else:
		global activation
		form = LogInForm(request.POST)
		if request.method == "POST":
			if form.is_valid():
				log = form.cleaned_data['Username']
				password = form.cleaned_data['Password']
				if (str(log), str(password)) in LogIn.objects.values_list('Username', 'Password'):
					activation = list(LogIn.objects.values_list('Username', 'Password')).index((str(log), str(password)))+1
					return redirect('estimator.views.estimate_admin') 
				else:
					raise ValidationError('Неверный логин или пароль!')
		else:
			form = LogInForm()

	return render(request, 'estimator/login.html', {'form': form})	 
	   
def estimate_admin(request):
	if activation:
		global num, num_form, surname, num_sel
		message = ""

		
		

		if request.method == "POST":
			form_info = ClientsInfoForm(request.POST)
			form_hist = ClientsHistForm(request.POST)	
			form_job = ClientsJobForm(request.POST)
			form_surname = SurnameForm(request.POST)
			
			if form_info.is_valid() and form_job.is_valid():
				second_name = form_info.cleaned_data['second_name']
				first_name = form_info.cleaned_data['first_name']
				third_name = form_info.cleaned_data['third_name']
				email = form_info.cleaned_data['email']
				birth = form_info.cleaned_data['birth']
				passport = form_info.cleaned_data['passport']
				work_place = form_job.cleaned_data['work_place']
				salary = form_job.cleaned_data['salary']
				experience = form_job.cleaned_data['experience']	
				
				with con:
					cur = con.cursor()    
					cur.execute("Select passport FROM black_list")         
					rows = cur.fetchall()
					
				if (int(passport),) in rows:
					message = "Клиент с такими паспортными данными находится в черном списке."	
				else:
					if client_info.objects.filter(passport=passport).count() == 0:
						client_info.objects.create(
													id_author=activation, 
												    second_name=second_name, 
												    first_name=first_name , 
												    third_name=third_name, 
												    email=email, 
												    birth=birth, 
												    passport=passport
												   )					
						client_job.objects.create(
													id_client=client_info.objects.count()+1, 
													work_place=work_place, 
													salary=salary, 
													experience=experience
												 )					
						message = "Новый клиент добавлен в базу. "
					else:
						message = "Клиент с такими паспортными данными сузествует в базе."					

			
			if form_hist.is_valid():
				passport = form_hist.cleaned_data['passport']
				start_credit = form_hist.cleaned_data['start_credit']
				finish_credit = form_hist.cleaned_data['finish_credit']
				amount = form_hist.cleaned_data['amount']
				number_of_delays = form_hist.cleaned_data['number_of_delays']
				status = form_hist.cleaned_data['status']
				
				client_info.objects.filter(passport=int(passport)).values_list('Id', flat=True)[0]
				
				
				if client_info.objects.filter(passport=int(passport)).values_list('Id', flat=True):
					client_history.objects.create(
												  Id_client=client_info.objects.filter(passport=int(passport)).values_list('Id', flat=True)[0], 
												  start_credit=start_credit, 
												  finish_credit=finish_credit, 
												  amount=amount, 
												  number_of_delays=number_of_delays, 
												  status=status
												  )
					message = "Информация о кредите добавлена в кредитную историю клиента. "					
				else:
					message = "В базе отсутствует клиент, с такими паспортными данными."
			
			if form_surname.is_valid():
				if str(form_surname.cleaned_data['Second_Name']) != "":
					surname = str(form_surname.cleaned_data['Second_Name'])
		else: 
			form_info = ClientsInfoForm()
			form_hist = ClientsHistForm()	
			form_job = ClientsJobForm()
			form_surname = SurnameForm()
		
		if 'add_client' in request.POST:
			num_form = 1
		
		if 'add_credit' in request.POST:
			num_form = 2	

		a = num
		if 'id_sub' in request.POST:
			num = int(request.POST.get('id_sub'))
		if a == num:
			num = 0
	
		if 'id_del' in request.POST:
			client_info.objects.filter(Id=int(request.POST.get('id_del'))).delete()	
			client_job.objects.filter(id_client=int(request.POST.get('id_del'))).delete()	
			client_history.objects.filter(Id_client=int(request.POST.get('id_del'))).delete()	
		
		b = num_sel
		if 'id_sel' in request.POST:
			num_sel = int(request.POST.get('id_sel'))
		if b == num_sel:
			num_sel = 0

		
		history = client_history.objects.filter(Id_client=num)

		return render(request, 'estimator/estimate_admin.html', {
																 'posts': zip(client_job.objects.all(), client_info.objects.all()), 
																 'form_hist': form_hist, 
																 'form_info': form_info, 
																 'form_job': form_job, 
																 'num': num, 
																 'history': history, 
																 'num_form': num_form, 
																 'message': message, 
																 'SurnameForm': form_surname, 
																 'Selected_Client': client_info.objects.filter(second_name=surname), 
																 'sel_history': client_history.objects.filter(Id_client=num_sel), 
																 'num_sel': num_sel
																})
																
	else:
		return redirect('estimator.views.estimate_login')

	
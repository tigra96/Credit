from django.shortcuts import render
from .forms import RequestForm
from django.shortcuts import render, get_object_or_404
from .models import Estimate
from django.contrib import messages
from django.shortcuts import redirect
#from .RFClassifier import Classifier


import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def Classifier(test):
    data = pd.read_csv('complete.csv', sep=',', header=None)
    RFClassifier = RandomForestClassifier(n_estimators=500)
    
    y = data[1]
    data.drop([0, 1], axis=1, inplace=True)
    
    RFClassifier.fit(data, y)
    return RFClassifier.predict(test)[0]



# Create your views here.

def estimator_list(request):
	return render(request, 'estimator/estimator_list.html', {})
	
def post_new(request):
	form = RequestForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			# exp = form.cleaned_data['experience']
			
			salary = form.cleaned_data['salary']
			age = form.cleaned_data['age']
			summ = form.cleaned_data['summ']	
			time = form.cleaned_data['time']
			experience = form.cleaned_data['experience']
			history = form.cleaned_data['history']
			current = form.cleaned_data['current']
			outstanding = form.cleaned_data['outstanding']
			
			a = Classifier([salary, age, summ, time, experience, history, current, outstanding])
			f = open('text.txt', 'w')
			f.write(str(a))
			#f.write(str(Classifier([50000, 25, 90000, 80, 60, 1, 1, 0])))
			f.close()	
			if (a == 1):
				return redirect('estimator.views.estimate_result')
			else:
				return redirect('estimator.views.estimate_bad_result')
	else:
		form = RequestForm()
	return render(request, 'estimator/post_edit.html', {'form': form})
	
def estimate_result(request):
       return render(request, 'estimator/estimate_result.html')
	   
def estimate_bad_result(request):
       return render(request, 'estimator/estimate_bad_result.html')

"""
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
	
"""
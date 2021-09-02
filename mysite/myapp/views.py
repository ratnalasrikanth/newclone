from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import os
import glob

# Create your views here.


def home(request):
	return HttpResponse("<h1>Welcome</h1><a href={}>click here to see result</a>".format('/home/result/'))

def ConvertCSVToJSON(request):
	print(glob.glob(str(os.getcwd()+'/*')))
	fobj = open(r'/app/office.csv', 'r')
	keys = ['label','id','link','children']

	complete_dic = {}
	parent = True
	for row in fobj.readlines()[1:]:
		fchild=True
		row = row.strip()
		if row.strip():
			if parent:
				dic = dict(zip(keys, row.split(',')[1:4] + [list()]))
				complete_dic.update(dic)
				parent = False
			else:
				firstchild = complete_dic['children']
				line = row.split(',')[1:]
				i=0
				while i<len(line):
					dic = dict(zip(keys, line[i:i+3] + [list()]))
					i+=3
					if dic['id'] == complete_dic["id"]:
						continue
					firstchild.append(dic)
					firstchild = dic.get('children')

	json_encode = json.dumps(complete_dic)
	json_object = json.loads(json_encode)
	k = json.dumps(json_object,indent=4)
	return HttpResponse(k)
	

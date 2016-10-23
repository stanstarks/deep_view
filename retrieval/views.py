import os
import numpy as np

from .models import Datum

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

test_dir = os.path.dirname(__file__) + '/test'

# data_dir = '/home/nisp/data/pornographic/JPEGImages'
data_dir = os.path.join(test_dir, 'img')

# predicts = np.load('/home/nisp/hzyangxudong/src/'+''+'predicts.npy')
predicts = np.load(test_dir + '/predicts.npy')

# list_path = '/home/nisp/hzyangxudong/src/test.txt'
list_path = os.path.join(test_dir, 'test.txt')
files = [line.split(' ')[0] for line in open(list_path).readlines()]

# res_path = '/home/nisp/hzyangxudong/src'
res_path = test_dir
model_register = {}

# Create your views here.
def index(request):
    global files
    list_path = '/home/nisp/hzyangxudong/src/test.txt'
    # file_list = [os.path.join(data_dir, file_name) for file_name in os.listdir(data_dir) ]
    sub_file_list = files[:3]
    #print file_list
    return render(request, 'retrieval/index.html', {'file_list': sub_file_list})

# TODO: add sync for thread safety
def load_resources(model_register, model_name):
    global res_path
    inds_path = os.path.join(res_path, model_name+'_'+'inds.npy')
    print inds_path
    if os.path.exists(inds_path):
        similar_inds = np.load(os.path.join(res_path, model_name+'_'+'inds.npy'))
        model_register[model_name] = {}
        model_register[model_name]['sim_inds'] = similar_inds
        return True
    else:
        return False

def calc_page_range(page_id, page_count):
    start_page_id = page_id - page_count / 2
    if start_page_id > 1:
        return range(start_page_id, start_page_id + page_count)
    else:
        return range(1, 1 + page_count)

def similar_image(request, model_name, page_id):
    global predicts, files, model_register
    if model_name not in model_register:
        ret = load_resources(model_register, model_name)
        if not ret:
            return HttpResponse("Error resources not found for model " + model_name)

    result_per_query = 8
    wrong_predicts_ind = predicts[0, :] != predicts[1, :]
    sub_inds = model_register[model_name]['sim_inds'][wrong_predicts_ind, :result_per_query+1]

    count_per_page = 5
    page_id = int(page_id)
    page_count = len(sub_inds) / count_per_page
    if page_id > (page_count + 1) or page_id < 1:
        return HttpResponse('Invalid Page Number!')
    sub_inds = sub_inds[(page_id-1)*count_per_page:page_id*count_per_page, :]
    data_lists = []
    for inds in sub_inds:
        query_datum = Datum(files[inds[0]], str(predicts[0, inds[0]]), str(predicts[1, inds[0]]))
        data_row = {'query': query_datum, 'results': []}
        for itt in range(1, len(inds)):
            ind  = inds[itt]
            datum = Datum(files[ind], str(predicts[0, ind]), str(predicts[1, ind]))
            data_row['results'].append((itt-1, datum))
        data_lists.append(data_row)

    page_range = calc_page_range(page_id, 20)
    context = dict(data_lists=data_lists,
                   model_name=model_name,
                   page_id=page_id,
                   page_range=page_range)
    return render(request, 'retrieval/similar.html', context)

def query(request):
    return render(request, 'retrieval/query.html')

def find_similar(request):
    return HttpResponse("")
    

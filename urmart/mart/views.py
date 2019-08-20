from django.shortcuts import render,redirect, HttpResponse
import db
# from django.contrib.auth.decorators import login_required
from functools import wraps

import json


import datetime

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

def check_is_login(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            if request.session['account']:
                return function(request, *args, **kwargs)
        except:
            return redirect('/urmart/loggin/')
    return wrap

def check_is_login_ajax(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            if request.session['account']:
                return function(request, *args, **kwargs)
        except:
            output_data = {}
            output_data['code'] = 401
            output_data['msg'] = 'not login'
            output = json.dumps(output_data)
            return HttpResponse(output, content_type="application/json")
    return wrap


def shopping(request):
    product_list = db.exec_sql_with_header("SELECT * FROM product")
    order_list = []
    member_id = 0
    try:
        member_id = request.session['member_id']
        order_list = db.exec_sql_with_header("SELECT * FROM oo WHERE member_id = " + str(member_id))
    except:
        pass
    return render(request, 'shopping.html', {'product_list':product_list,'order_list':order_list})

def loggin(request):
    return render(request, 'loggin.html')

def loggin_action(request):
    account = request.POST.get('account', '')
    pwd = request.POST.get('pwd', '')
    result = db.exec_sql_with_header("SELECT * FROM member where account = '"+account+"' and pwd = '"+pwd+"'  ")
    if result:
        request.session['member_id'] = result[0]['member_id']
        request.session['account'] = result[0]['account']
        request.session['is_vip'] = result[0]['is_vip']

        print("GREAT")
        print(request.session['account'])
        print(request.session['is_vip'])

        return redirect('/urmart/shopping/')
    else:
        return redirect('/urmart/loggin/')

def logout_action(request):
    del request.session['member_id']
    del request.session['account']
    del request.session['is_vip']
    return redirect('/urmart/loggin/')

def product_list_ajax(request):
    result = db.exec_sql_with_header("SELECT * FROM product")

    output_data = {}
    output_data['code'] = 200
    output_data['msg'] = 'ok'
    output_data['data'] = result
    output = json.dumps(output_data)
    return HttpResponse(output, content_type="application/json")

# @check_is_login_ajax
def order_list_ajax(request):
    member_id = request.session['member_id']
    result = db.exec_sql_with_header("SELECT * FROM oo WHERE member_id = " + str(member_id))

    output_data = {}
    output_data['code'] = 200
    output_data['msg'] = 'ok'
    output_data['data'] = result
    output = json.dumps(output_data,sort_keys=True,indent=1,default=default)
    return HttpResponse(output, content_type="application/json")

@check_is_login
def ccc(request):
    print("CCCC")
    return render(request, 'ccc.html', {'data': 'hello'})

@check_is_login_ajax
def place_order_ajax(request):
    pid = request.POST.get('pid', '')
    num = int(request.POST.get('num', ''))

    output_data = {}
    output_data['code'] = 200
    output_data['msg'] = 'ok'

    if num == '':
        output_data['code'] = 203
        output_data['msg'] = 'bad number'
        output = json.dumps(output_data)
        return HttpResponse(output, content_type="application/json")

    result = db.exec_sql_with_header("SELECT * FROM product where product_id='"+pid+"'")
    member_id = request.session['member_id']
    account = request.session['account']
    is_vip = request.session['is_vip']
    require_vip = result[0]['vip']
    remain_number = result[0]['stock_pcs']
    product_id = result[0]['product_id']
    price = result[0]['price']
    shop_id = result[0]['shop_id']

    if require_vip == 1 and is_vip == 0:
        output_data['code'] = 201
        output_data['msg'] = 'not vip'
        output = json.dumps(output_data)
        return HttpResponse(output, content_type="application/json")

    if remain_number < num:
        output_data['code'] = 202
        output_data['msg'] = 'not enough'
        output = json.dumps(output_data)
        return HttpResponse(output, content_type="application/json")


    order_price = num * price
    # place order
    SQL = "INSERT INTO oo (member_id,product_id,order_price,product_num,shop_id) VALUES ('"+str(member_id)+"','"+str(product_id)+"','"+str(order_price)+"','"+str(num)+"','"+shop_id+"')"
    db.exec_sql_with_commit(SQL)
    SQL = "UPDATE product SET stock_pcs = stock_pcs - " + str(num) + " WHERE product_id = " + str(product_id)
    # SQL = "UPDATE product SET stock_pcs = stock_pcs + " + str(num)
    db.exec_sql_with_commit(SQL)


    # output_data['data'] = result
    output = json.dumps(output_data)
    return HttpResponse(output, content_type="application/json")

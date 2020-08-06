from django.shortcuts import render
from . import rpc
from iconsdk.exception import JSONRPCException
from .models import Cars, Users
from django.http import HttpResponse
import json
import datetime
from django.shortcuts import redirect
from django.urls import reverse


def set_wallet_session(request, wallet_address):
    request.session['wallet_address'] = wallet_address
    Users.objects.update_or_create(user_wallet=wallet_address)
    return HttpResponse(json.dumps({'wallet_address': request.session['wallet_address']}), content_type="applicaiton/json")


def market_index(request):
    if 'wallet_address' not in request.session:
        request.session['wallet_address'] = 'null'

    # Get car basic data from local DB
    all_cars = Cars.objects.filter(car_forsale="on")

    context = {}
    context["wallet_address"] = request.session["wallet_address"]
    context["all_cars"] = all_cars    

    return render(request, 'market/market_index.html', context)


def market_cardetail(request, id):
    car = Cars.objects.filter(car_id=id).first()

    # Get NFT details from the blockchain
    params = {
        "_tokenId": id,
    }
    try:
        car_onchain = rpc.RPC().rpc_call("get_the_token", params)
        car_owner = rpc.RPC().rpc_call("ownerOf", params)
        car_operator = rpc.RPC().rpc_call("getApproved", params)
    except JSONRPCException as e:
        print(str(e.message))

    params = {}
    try:
        price = rpc.RPC().rpc_call_band("get_price", params)
        multiplier = rpc.RPC().rpc_call_band("get_multiplier", params)
    except JSONRPCException as e:
        print(str(e.message))

    icx_usd = int(price, 0) / int(multiplier, 0)    

    context = {}
    context["car_id"] = id
    context["wallet_address"] = request.session["wallet_address"]
    context["car"] = car    
    context["car_onchain"] = car_onchain
    context["car_owner"] = car_owner
    context["car_operator"] = car_operator
    context["icx_usd"] = icx_usd
    return render(request, 'market/market_cardetail.html', context)


def make_transfer(request):

    old_owner = request.POST["old_owner"]
    new_owner = request.POST["new_owner"]
    car_id = request.POST["car_id"]

    params = {
        "_from": old_owner,
        "_to": new_owner,
        "_tokenId": car_id,
    }
    try:
        rpc.RPC().rpc_call_transaction("transferFrom", params)
    except JSONRPCException as e:
        print(str(e.message))
    
    Cars.objects.filter(car_id=car_id).update(car_boughtat=datetime.datetime.now())

    redirect_url = reverse('garage_index', args=[new_owner])    
    return HttpResponse(json.dumps({'redirect_url': redirect_url}), content_type="applicaiton/json")    
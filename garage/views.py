from django.shortcuts import render
from market.rpc import RPC
from iconsdk.exception import JSONRPCException
from market.models import Cars
from django.http import HttpResponseRedirect
from django.urls import reverse

def garage_index(request, wallet):

    # Get cars of owner from the blockchain
    params = {
        "_owner": wallet,
    }
    try:
        owner_cars = RPC().rpc_call("get_tokens_of_owner", params)
    except JSONRPCException as e:
        print(str(e.message))

    car_list = []
    for hex_id in owner_cars["owned_tokens"]:
        int_id = int(hex_id, 16)
        car = Cars.objects.filter(car_id=int_id).first()
        
        params = {
            "_tokenId": int_id,
        }
        try:
            car_onchain = RPC().rpc_call("get_the_token", params)
        except JSONRPCException as e:
            print(str(e.message))
        car.car_onchain = car_onchain

        car_list.append(car)

    context = {}
    context["wallet"] = wallet
    context["car_list"] = car_list

    return render(request, 'garage/garage_index.html', context)


def garage_sell(request, car_id):
    if request.method == 'POST':
        # Update local database
        car_id = request.POST["car_id"]
        car_headline = request.POST["car_headline"]
        car_description = request.POST["car_description"]
        car_price = request.POST["car_price"]
        car_forsale = request.POST.get("car_forsale", "off")

        car = Cars.objects.get(car_id=car_id)
        car.car_headline = car_headline
        car.car_description=car_description
        car.car_price = car_price
        car.car_forsale = car_forsale
        car.save()

        #context = {}
        return HttpResponseRedirect(reverse('market_index'))
        #return render(request, 'garage/garage_sell.html', context)
    else:
        car = Cars.objects.filter(car_id=car_id).first()
        context = {}
        context["car"] = car
        context["wallet_address"] = request.session["wallet_address"]
        return render(request, 'garage/garage_sell.html', context)
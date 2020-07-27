from django.shortcuts import render
from market.models import Cars
from market.rpc import RPC
from iconsdk.exception import JSONRPCException
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def mint_car(request):
    if request.method == 'POST':

        # do id validation and redirect
        cc = Cars.objects.filter(car_id=request.POST["_tokenId"])
        if(cc.count() > 0):
            return render(request, 'management/mint_car.html', {'alert_flag': True})

        # Blockchain
        _to = request.POST["_to"]
        _tokenId = request.POST["_tokenId"]
        _manufacturer = request.POST["_manufacturer"]
        _year = request.POST["_year"]
        _model = request.POST["_model"]
        _country = request.POST["_country"]
        _hp = request.POST["_hp"]
        _torque = request.POST["_torque"]
        _displacement = request.POST["_displacement"]

        params = {
            "_to": _to,
            "_tokenId": _tokenId,
            "_manufacturer": _manufacturer,
            "_year": _year,
            "_model": _model,
            "_country": _country,
            "_hp": _hp,
            "_torque": _torque,
            "_displacement": _displacement,
        }

        try:
            RPC().rpc_call_transaction("mint", params)
        except JSONRPCException as e:
            print(str(e.message))        

        # Database  
        car = Cars()    
        car.car_id = request.POST["_tokenId"]
        car.car_year_name = _year + " " + _manufacturer + " " + _model
        car.car_photo = request.FILES["car_photo"]     
        car.car_headline = request.POST["car_headline"]
        car.car_description = request.POST["car_description"]
        car.car_price = request.POST["car_price"]
        car.car_forsale = request.POST["car_forsale"]
        car.car_boughtat = datetime.datetime.now()
        car.save()
        

    return render(request, 'management/mint_car.html')

def mint_part(request):
    # update smart contract with mint_part method
    return render(request, 'management/mint_part.html')


def make_transfer(request):

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

    return HttpResponse(json.dumps({'car_id': request.POST["car_id"]}), content_type="applicaiton/json")
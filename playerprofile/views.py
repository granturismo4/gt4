from django.shortcuts import render
from market.models import Users, Cars
from market.rpc import RPC
from iconsdk.exception import JSONRPCException

# Create your views here.
def playerprofile_index(request, wallet):
    playerprofile = Users.objects.filter(user_wallet=wallet).first()

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
    context["playerprofile"] = playerprofile
    context["car_list"] = car_list
    return render(request, 'playerprofile/playerprofile_index.html', context)
import moncash

from moncash.exceptions import NotFoundError

gateway = moncash.Moncash(
        client_id="26c0da72fb39f2219066e793663e133a",
        client_secret="eDW4R0KpN8UYQheoEX_OBwAztXqewARKbKevjwdkzm1gLlGGouzdv1znWpLNhuJ_",
        environment=moncash.environment.Sandbox
    )

# get_paid_url = gateway.payment.create(
#     amount=250,
#     reference=30
# )

# print(get_paid_url)

try:
    resp = gateway.payment.get_by_ref(483)
except NotFoundError:
    print("On a pas trouvé ce paiemetn")

#print(resp)


# TODO:  in your app redirect the user to the payment url to get paid
    

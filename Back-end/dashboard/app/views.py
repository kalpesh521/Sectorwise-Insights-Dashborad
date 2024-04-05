from django.http import JsonResponse
from .models import energy_collection

 
def get_data(request):
    data = list(energy_collection.find())   
    for doc in data:
        doc['_id'] = str(doc['_id'])
    return JsonResponse(data, safe=False) 
 
from .serializers import * 

def validate_api(request):
    res = {}
    res["success"] = True
    res["errors"] = None
    res["details"] = None
    validation = CpfSerializer(data=request)
    if validation.is_valid():
        res["success"] = True
    else:
        res["success"] = False
        res["details"] = "Bad Request"
        res["errors"] = validation.errors
    return res

def validate_creation(request):
    res = {}
    res["success"] = True
    res["errors"] = None
    res["details"] = None
    validation = CpfSerializer(data=request)
    if validation.is_valid():
        res["success"] = True
        res["status"] = 200
        validation.save()
    else:
        res["success"] = False
        res["details"] = "Bad Request"
        res["errors"] = validation.errors
        res["status"] = 404
        if validation.data.get('status') == 'DENY':
            res["details"] = "CPF DENIED"
            res["errors"] = "CPF DENIED IN DATABASE"
            res["status"] = 500
    return res
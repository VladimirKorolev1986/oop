def dd(request):
    if request.get('method') is None or request.get('method') == 'GET':
        return 'GET'
    return None


d = {"method": "GET", "url": "contact.html"}

print(dd(d))
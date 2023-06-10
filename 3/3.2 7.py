class HandlerGET:
    """класс декоратор"""

    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        if request.get('method') is None or request.get('method') == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        x = func(request)
        return f"GET: {x}"


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})

print(res)

from django.http import HttpResponse
from datetime import datetime


def test(request):
    now = datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)

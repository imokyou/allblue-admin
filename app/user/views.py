import json
from django.http import HttpResponse
from datetime import datetime
from lib import permissions


def test(request):
    # now = datetime.now()
    # current_url = request.META['REQUEST_URI']
    # html = "<html><body>It is now %s<br>%s</body></html>" % (now, current_url)
    current_uri = request.META['REQUEST_URI'].split('?')[0].split('/')
    current_uri = '/%s/' % '/'.join([x for x in current_uri if x])
    data = {'uri': current_uri}
    return HttpResponse(json.dumps(data))


def page_list(request):
    menus = permissions.get_user_menu(request)
    data = {'menus': menus}
    return HttpResponse(json.dumps(data))

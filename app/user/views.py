from lib import utils


def test(request):
    current_uri = request.META['REQUEST_URI'].split('?')[0].split('/')
    current_uri = '/%s/' % '/'.join([x for x in current_uri if x])
    data = {'uri': current_uri}
    return utils.HttpJsonResponse(data)


def page_list(request):
    return utils.HttpRender(request, 'user/list.html')

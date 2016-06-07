from lib import utils


def index(request):
    return utils.HttpRender(request, 'layout/index.html')

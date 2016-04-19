from django.shortcuts import render_to_response
from django.template import RequestContext


def test(request):
    if request.method == 'POST':
        text = request.POST['text']
        if text == 'test':
            return render_to_response('test_post.html')
    return render_to_response('test.html', RequestContext(request))

def index(request):
    return render_to_response('index.html', RequestContext(request))


def services(request):
    return render_to_response('test.html', RequestContext(request))
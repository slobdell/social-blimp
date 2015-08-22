import json

from django.http import Http404
from django.http import HttpResponse


def render_to_json(response_obj, context={}, content_type="application/json", status=200):
    json_str = json.dumps(response_obj, indent=4)
    return HttpResponse(json_str, content_type=content_type, status=status)


def requires_post(fn):
    def inner(request, *args, **kwargs):
        if request.method != "POST":
            return Http404
        post_data = request.POST or json.loads(request.body)
        kwargs["post_data"] = post_data
        return fn(request, *args, **kwargs)
    return inner


def requires_auth(fn):
    def inner(request, *args, **kwargs):
        if 'username' not in request.GET:
            return render_to_json({
                "message": "GET requires a 'username'"
            }, status=400)
        username = request.GET['username']
        user = User.get_by_username(username)

        if 'access_token' not in request.GET:
            return render_to_json({
                "message": "GET requires an 'access_token'"
            }, status=400)
        access_token = AccessToken.get_from_token_data(request.GET['access_token'])
        if not access_token.has_access_to_user(user):
            return render_to_json({
                "message": "Invalid Access Token"
            }, status=403)
        kwargs['user'] = user

        return fn(request, *args, **kwargs)
    return inner

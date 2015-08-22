# import datetime
import json
# import os

# from django.conf import settings
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render_to_response


def render_to_json(data, status=200):
    return HttpResponse(json.dumps(data), content_type="application/json", status=status, mimetype='application/json')


def global_render_to_response(template, render_data):
    if "JSContext" not in render_data:
        render_data["JSContext"] = "{}"
    return render_to_response(template, render_data)


def muscle(request, muscle_name):
    render_data = {
    }
    return global_render_to_response("basic_navigation/muscle_group.html", render_data)


def exercise(request, exercise_name):
    render_data = {
    }
    return global_render_to_response("basic_navigation/exercise.html", render_data)


def home(request):
    JSContext = {
    }
    render_data = {
        "JSContext": json.dumps(JSContext)
    }
    return global_render_to_response("basic_navigation/search_engine_content.html", render_data)

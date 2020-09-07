from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from api.services import getters


class HashView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def hash(self, request):
        return Response(getters.get_hash())


class EvennessWeek(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def evenness(self, requests):
        return Response(getters.get_current_week_evenness_as_json())


class GroupView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        return Response(getters.get_all_groups_as_json())


class TimetableView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def timetable(self, request, obj_id):
        return Response(getters.get_timetable(obj_id))
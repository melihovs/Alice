from django.views.decorators.csrf import csrf_exempt
from django.template.defaulttags import register
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from maze.models import Mazegen, GrowingTree, MazeDumper
import re
import json
import logging

logging.basicConfig(filename="/home/evostrov/py/debug.log", level=logging.INFO)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def last_maze(request):
    maze_json_dump = MazeDumper.objects.order_by('-id')[0].maze_json_dump
    maze = json.loads(maze_json_dump)

    return render(request, 'last_maze.html', {'maze': maze, 'size_range': range(settings.MAZE_SIZE), 'size': settings.MAZE_SIZE})

def generate_maze(request):
    maze_gen = GrowingTree(size=settings.MAZE_SIZE)
    maze_gen.generate_maze()

    dumper = MazeDumper(maze_json_dump=maze_gen.to_json())
    dumper.save()

    response_data = {
        'maze_dump' : maze_gen.dump(),
        'size' : settings.MAZE_SIZE,
    }

    return JsonResponse(response_data)

def get_person_position(request):
    maze_obj = MazeDumper.objects.order_by('-id')[0]

    res = {
        'node_row': maze_obj.cur_node_row,
        'node_col': maze_obj.cur_node_col,
        'dir': maze_obj.cur_direction,
    }

    return JsonResponse(res)

@csrf_exempt
def update_person_position(request):
    params = request.body.split('&');

    res = {}
    for param in params:
        match = re.match( '(\w+)=(.+)', param )
        res[ match.group(1) ] = match.group(2)

    maze_obj = MazeDumper.objects.order_by('-id')[0]
    maze_obj.cur_node_row = res['node_row']
    maze_obj.cur_node_col = res['node_col']
    maze_obj.cur_direction = res['dir']
    maze_obj.save()

    return HttpResponse('')

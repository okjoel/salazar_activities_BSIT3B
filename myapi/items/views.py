from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Item

# Get all items or search by name
def get_items(request):
    search_query = request.GET.get('search', '')

    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
    else:
        items = Item.objects.all()

    data = [{"id": item.id, "name": item.name, "description": item.description} for item in items]
    return JsonResponse({"items": data}, safe=False)

# Get a single item by ID
def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        data = {"id": item.id, "name": item.name, "description": item.description}
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({"error": "Item not found"}, status=404)

# Add a new item
@csrf_exempt
def add_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        name = data.get("name")
        description = data.get("description", "")

        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)

        item = Item.objects.create(name=name, description=description)
        return JsonResponse({"message": "Item added", "id": item.id}, status=201)

# Update an existing item
@csrf_exempt
def update_item(request, item_id):
    if request.method == "PUT":
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        item.name = data.get("name", item.name)
        item.description = data.get("description", item.description)
        item.save()

        return JsonResponse({"message": "Item updated", "id": item.id})

# Delete an item
@csrf_exempt
def delete_item(request, item_id):
    if request.method == "DELETE":
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JsonResponse({"message": "Item deleted"})
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)

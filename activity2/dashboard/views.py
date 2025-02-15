from django.shortcuts import render

def dashboard_view(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    return render(request, 'dashboard/dashboard.html', {'data': data})

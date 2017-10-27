from django.shortcuts import render
# from django.http import HttpResponse


def my_view(request):
    value = request.GET.get('key', 'HEY')
    context = {
        'message': value
    }
    return render(request, 'my_template.html', context)

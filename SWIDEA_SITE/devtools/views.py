from django.shortcuts import render, redirect, get_object_or_404
from .models import DevTool

# Create your views here.
def devtool_list(request):
    devtools = DevTool.objects.all() 
    return render(request, 'devtools/devtool_list.html', {"devtools":devtools})

def devtool_detail(request, devtool_id):
    devtool = get_object_or_404(DevTool, id = devtool_id)
    return render(request, 'devtools/devtool_detail.html',
    {'devtool':devtool})

def devtool_create(request):
    if request.method == "POST":
        devtool = DevTool.objects.create(
            name = request.POST["name"],
            kind = request.POST['kind'],
            content = request.POST['content'],
        )
        return redirect('devtools:detail', devtool.id)
    return render(request, 'devtools/devtool_form.html')

def devtool_update(request, devtool_id):
    devtool = get_object_or_404(DevTool, id = devtool_id)

    if request.method == "POST":
        devtool.name = request.POST["name"]
        devtool.kind = request.POST['kind']
        devtool.content = request.POST['content']
        devtool.save()

        return redirect('devtools:detail', devtool.id)

    return render(request, 'devtools/devtool_form.html', {
        'devtool': devtool
    })

def devtool_delete(request, devtool_id):
    devtool = get_object_or_404(DevTool, id=devtool_id)
    devtool.delete()
    return redirect('devtools:list')

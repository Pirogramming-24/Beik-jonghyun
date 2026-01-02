from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse  
from django.db.models import Count    
from .models import Idea, IdeaStar
from .forms import IdeaForm

def idea_list(request):
    sort = request.GET.get('sort', 'recent')
    ideas = Idea.objects.all()

    if sort == 'recent':
        ideas = ideas.order_by('-created_at')
    elif sort == 'old':
        ideas = ideas.order_by('created_at')
    elif sort == 'name':
        ideas = ideas.order_by('title')
    elif sort == 'star':
        ideas = ideas.annotate(star_count=Count('stars')).order_by('-star_count')

    starred_idea_ids = list(IdeaStar.objects.values_list('idea_id', flat=True))

    for idea in ideas:
        if idea.id in starred_idea_ids:
            idea.is_starred = True
        else:
            idea.is_starred = False

    return render(request, 'idea/idea_list.html', {'ideas': ideas, 'sort': sort})

def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    return render(request, 'idea/idea_detail.html', {'idea': idea})

def idea_create(request):
    form = IdeaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        idea = form.save()
        return redirect('idea:detail', idea.id)
    return render(request, 'idea/idea_form.html', {'form': form, 'mode': 'create'})

def idea_update(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    form = IdeaForm(request.POST or None, request.FILES or None, instance=idea)
    if form.is_valid():
        form.save()
        return redirect('idea:detail', idea.id)
    return render(request, 'idea/idea_form.html', {'form': form, 'mode': 'update'})

def idea_delete(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()
    return redirect('idea:list')


def update_interest(request, idea_id, direction):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, id=idea_id)
        if direction == 'up':
            idea.interest += 1
        else:
            idea.interest -= 1
        idea.save()
        return JsonResponse({'interest': idea.interest})
    return JsonResponse({'error': 'Bad Request'}, status=400)

def toggle_star(request, idea_id):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, id=idea_id)
        
        stars = IdeaStar.objects.filter(idea=idea)

        if stars.exists():
            stars.delete()  
            is_starred = False
        else:
            IdeaStar.objects.create(idea=idea)
            is_starred = True
        
        return JsonResponse({'is_starred': is_starred})
        
    return JsonResponse({'error': 'Bad Request'}, status=400)
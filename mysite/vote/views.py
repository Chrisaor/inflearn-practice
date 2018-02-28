from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from vote.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, 'vote/index.html', context)

def detail(request, pk):
    try:
        q = get_object_or_404(Question, pk=pk)
    except Question.DoesNotExist:
        raise Http404(f'Question {pk} does not exist')

    context = {
        'question': q,
    }
    return render(request, 'vote/detail.html', context )

def vote(request, pk):
    question = get_object_or_404(Question, pk = pk)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        context = {
            'question':question,
            'error_message': 'ERROR'
        }
        return render(question, 'vote/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('vote:result', pk=pk)

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question':question,
    }
    return render(request, 'vote/results.html', context)

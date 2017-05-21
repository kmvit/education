from .models import Quiz, Question, Score
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    latest_quiz = Quiz.objects.all().order_by('-created')[:5]
    return render_to_response('quiz/index.html', {'latest_quiz': latest_quiz})
    
def detail(request, quiz_id):
    q = get_object_or_404(Quiz, pk=quiz_id)
    context = {'quiz': q}
    return render(request, 'quiz/detail.html', context)

def results(request, quiz_id):
    return HttpResponse("You're looking at the results of quiz %s." % quiz_id)

def do(request, quiz_id):
    q = get_object_or_404(Quiz, pk=quiz_id)
    try:
        answer = ''
        for question in q.question_set.all():
            answer += request.POST['q%d' % question.id]
    except (KeyError, Question.DoesNotExist):
        # Redisplaying the form
        context = {
            'quiz': q,
            'error_message': "You didn't do the quiz %r " %request.POST,
        }
        return render(request,'quiz/detail.html',context)
    else:
        # request.user masih gagal karena belum diimport
        s = q.score_set.create(student=request.user.username, submit_answer=answer, score=100)
        s.save()
        return redirect(results, args=(q.id,))
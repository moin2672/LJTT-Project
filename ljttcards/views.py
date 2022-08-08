from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ljttcards.forms import LJTTCardForm, LessonForm
from .models import LJTTCard, Lesson
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class LJTTCardListView(ListView):
    model = LJTTCard
    context_object_name = "cards"
    template_name = "ljttcards/ljttcards_list.html"

    # def get_queryset(self):
    #     return self.request.user.notes.all()  #to get only the selected user notes. Reference: http://ccbv.co.uk/projects/Django/4.0/django.views.generic.list/ListView/

class LJTTCardDetailView(DetailView):
    model = LJTTCard
    context_object_name = "card"
    #template_name = "ljttcards/ljttcard_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LJTTCardDetailView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(LJTTCard, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context["total_likes"]=total_likes
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"]=liked
        return context

class LJTTCardCreateView(LoginRequiredMixin, CreateView):
    model= LJTTCard
    form_class =LJTTCardForm
    # fields = '__all__'
    #template_name = "ljttcards/ljttcard_form.html"
    login_url = "/login"

    def form_valid(self, form): #stops the form from submitting and assigning the user to it for cleaned_data() called by form.is_valid() 
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class LJTTCardUpdateView(LoginRequiredMixin, UpdateView):
    model= LJTTCard
    form_class =LJTTCardForm
    # fields = '__all__'
    #template_name = "ljttcards/ljttcard_form.html"
    login_url = "/login"

class LJTTCardDeleteView(LoginRequiredMixin, DeleteView):
    model = LJTTCard
    template_name = 'ljttcards/ljttcard_delete.html' # it can be avoided if the template name changed from 'notes_delete.html' to 'notes_confirm_delete.html
    success_url =  reverse_lazy('cards.list')  #'/ljtt/cards'
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        
@login_required(login_url = "/login")
def LikeView(request, pk):
    card = get_object_or_404(LJTTCard, id=request.POST.get('card_id')) #in html #id='card_id'
    liked = False
    if card.likes.filter(id=request.user.id).exists():
        card.likes.remove(request.user)
        liked = False
    else:
        card.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('cards.detail', args=[str(pk)]))

@login_required(login_url = "/login")
def MyLikedCardsView(request, pk):
    myLiked_cards = LJTTCard.objects.filter(likes__in=[pk])
    return render(request, 'ljttcards/ljttcard_liked_card.html', {'myLiked_cards':myLiked_cards, })

@login_required(login_url = "/login")
def LessonListView(request):
    lesson_list=Lesson.objects.all()
    # lesson_cards_count_list = [LJTTCard.objects.filter(lesson=lsn.id).count() for lsn in lesson_list]
    # lesson_cards_count_list = LJTTCard.objects.filter(lesson__in=lesson_list)
    return render(request, 'ljttcards/ljttcard_lessons.html', {'lesson_list':lesson_list})

class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model= Lesson
    form_class =LessonForm
    # fields = '__all__'
    #template_name = "ljttcards/lesson_form.html"
    login_url = "/login"

class LessonCreateView(LoginRequiredMixin, CreateView):
    model= Lesson
    form_class =LessonForm
    # fields = '__all__'
    #template_name = "ljttcards/lesson_form.html"
    login_url = "/login"

def LessonWiseLJTTCardView(request, lName_id):
    LessonWise_Cards = LJTTCard.objects.filter(lesson=lName_id)
    card_LessonName = Lesson.objects.get(pk=lName_id)
    lesson_cards_count_list= LessonWise_Cards.count()
    return render(request, 'ljttcards/ljttcard_lesson_wise_card.html', {'card_LessonName':card_LessonName, 'LessonWise_Cards':LessonWise_Cards, 'lesson_cards_count_list':lesson_cards_count_list })
from django import forms
from .models import LJTTCard, Lesson


class LJTTCardForm(forms.ModelForm):
    class Meta:
        model= LJTTCard
        fields = ('imageData', 'lesson', 'jp_word', 'en_word', 'en_pronounciation', 'ta_word', 'ta_pronounciation', 'hint')

    def __init__(self, *args, **kwargs):
        super(LJTTCardForm, self).__init__(*args, **kwargs)

        self.fields['imageData'].widget.attrs['class']='form-control'
        self.fields['lesson'].widget.attrs['class']='form-select'
        self.fields['jp_word'].widget.attrs['class']='form-control'
        self.fields['en_word'].widget.attrs['class']='form-control'
        self.fields['en_pronounciation'].widget.attrs['class']='form-control'
        self.fields['ta_word'].widget.attrs['class']='form-control'
        self.fields['ta_pronounciation'].widget.attrs['class']='form-control'
        self.fields['hint'].widget.attrs['class']='form-control'


class LessonForm(forms.ModelForm):
    class Meta:
        model= Lesson
        fields = ('lessonName', )

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)

        self.fields['lessonName'].widget.attrs['class']='form-control'
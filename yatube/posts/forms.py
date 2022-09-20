from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': 'Текст',
            'group': 'Группа',
        }

        def clean_text(self):
            data = self.cleaned_data['text']

            if data.lower() == "":
                raise forms.ValidationError('текст не должен быть пустым')
            return data

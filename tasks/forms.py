from django import forms


class LevelA(forms.Form):
    task_1_word_1 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_1',
        'class': 'form-control',
        'placeholder': '(1)',
    }))
    task_1_word_2 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_2',
        'class': 'form-control',
        'placeholder': '(2)',
    }))
    task_1_word_3 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_3',
        'class': 'form-control',
        'placeholder': '(3)',
    }))
    task_1_word_4 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_4',
        'class': 'form-control',
        'placeholder': '(4)',
    }))
    task_1_word_5 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_5',
        'class': 'form-control',
        'placeholder': '(5)',
    }))
    task_1_word_6 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_6',
        'class': 'form-control',
        'placeholder': '(6)',
    }))
    task_1_word_7 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_7',
        'class': 'form-control',
        'placeholder': '(7)',
    }))
    task_1_word_8 = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'label': 'word_8',
        'class': 'form-control',
        'placeholder': '(8)',
    }))

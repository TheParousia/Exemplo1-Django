from django.forms import ModelForm
from app1.models import Cartao


class ArticleForm(ModelForm):
    class Meta:
        model = Cartao

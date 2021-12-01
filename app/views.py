from django.shortcuts import render
from django.views.generic import View
from .models import Calendar
"""
#ここから選択肢 https://arakan-pgm-ai.hatenablog.com/entry/2019/02/18/090000
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.staticfiles.templatetags.staticfiles import static
from . import forms
from django.template.context_processors import csrf
#ここまで
"""

from .forms import ChoiceForm
from django.http import HttpResponse

#公式チュートリアルをやってみる
def index(request):
    #latest_calendar_list = Calendar.objects.order_by('-id')[:5]
    #context = {'latest_calendar_list': latest_calendar_list}
    
    params = {
        'form': ChoiceForm(),
        'check_result':None
    }
    if (request.method == 'POST'):
        if('check' in request.POST):
            params['form'] = ChoiceForm(request.POST)
            params['check_result'] = '<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=2&bgcolor=%23ffffff&ctz=Asia%2FTokyo&title=%E5%85%AC%E6%BC%94%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB&src=YXMydWZrcXBucmExc2J1ajgxanVuYjRnbWNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23D81B60" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
        else:
            params['check_result'] = 'チェックが入っていません。'
    return render(request, 'app/index.html', params)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        calendar_data = Calendar.objects.all()
        if calendar_data.exists():
            calendar_data = calendar_data.order_by('-id')[:5]
        return render(request, 'app/index.html', {'calendar_data' : calendar_data})





"""
#ここから選択肢 https://arakan-pgm-ai.hatenablog.com/entry/2019/02/18/090000

def demo3(request):
    labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']
    # 入力結果を格納する辞書
    results = {}
    radios = {}
    ret = ''
    if request.method == 'POST':
        # 入力されたデータの受取
        results = request.POST.getlist("two")
        ret = 'OK'
        c = {'results': results,'ret':ret}
    else:    
        form = forms.CheckboxForm()
        choice1 = [] 
        choice1.append(('1','動的選択肢１'))
        choice1.append(('2','動的選択肢２'))
        choice1.append(('3','動的選択肢３'))
        choice1.append(('4','動的選択肢４'))
        form.fields['four'].choices = choice1
        form.fields['four'].initial = ['2']    
        form.fields['five'].choices = choice1
        form.fields['five'].initial = ['3'] 
        c = {'form': form,'ret':ret}
        # CFRF対策（必須）
        c.update(csrf(request))
    return render(request,'index.html',c)
"""

#ここから　参考https://www.youtube.com/watch?v=VIUY95ewjSU
from .models import troupes

def displayschedule(request):
    result = troupes.objects.all()
    return render(request, 'app/index.html', {"troupes":result})


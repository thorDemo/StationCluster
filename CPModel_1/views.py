from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import NewsArticle, ListArticle


# @cache_page(60 * 60 * 2)
def index_page(request):
    template = loader.get_template('CPModel_1/index.html')
    new_article = NewsArticle.objects.order_by('?')[:30]
    list_article = ListArticle.objects.order_by('?')[:3]
    temp = 0
    for line in new_article:
        img = line.img.split(',')
        new_article[temp].img = img
        temp += 1
    content = {
        'new_article_10_1': new_article[:10],
        'new_article_10_2': new_article[10:20],
        'new_article_3_1':new_article[20:23],
        'new_article_3_2':new_article[23:26],
        'new_article_3_3':new_article[26:29],
        'list_article': list_article,
        'title': '香港生活_赌场游戏名字_大世界娱乐平台',
        'keywords': '最好平台，真人在线，香港生活，香港娱乐，香港赛马，香港美食',
        'description': '香港生活线上娱乐平台为您提供体育赛事，视讯直播，电子游艺，彩票游戏，香港娱乐，香港赛马，香港美食。香港生活是“亚洲最受玩家喜爱品牌”，如今也成为亚洲最具有领导地位的顶级娱乐平台，拥有15年资深行业经验，8项设计系统保障，在线玩家超过10000+，96%客户满意度，我们将竭诚为您服务，为您提供顶级娱乐享受。',
    }
    return HttpResponse(template.render(content, request))

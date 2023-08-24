from typing import Any, Optional
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        return reverse('articleapp:detail', kwargs={'pk':kwargs['pk']})
    
    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        like_record_exists = LikeRecord.objects.filter(user=user, article=article).exists()

        if like_record_exists:
            # 좋아요를 취소
            LikeRecord.objects.filter(user=user, article=article).delete()
            article.like -= 1
            article.save()
        else:
            # 좋아요를 추가
            LikeRecord(user=user, article=article).save()
            article.like += 1
            article.save()

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)

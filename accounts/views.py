from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from accounts.forms import SignupForm

import json
import logging
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.views import View
from django.core.cache import cache


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('top')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        messages.info(self.request, "ログインしました")
        login(self.request, self.object)
        return valid


CACHE_TIMEOUT = 60 * 10
logger = logging.getLogger(__name__)


class ValidateUsernameAjaxView(View):
    """ユーザー名が既に使われているかチェック"""

    def get(self, request, *args, **kwargs):
        key = "valid_username"
        cache_data = cache.get(key)
        username = request.GET.get('username')

        data = {
            'success': False,
            'message': "同じユーザー名が既に登録済みです。",
        }

        # キャシュが空
        if not cache_data:
            try:
                # 入力された名前が存在すればキャッシュに保存
                exist_username = get_user_model().objects.filter(username__iexact=username).get().username
                cache.set(key, exist_username, CACHE_TIMEOUT)
                logger.debug('名前をキャッシュに保存')

            except Exception:
                data['success'] = True
                data['message'] = ""
                logger.debug('キャッシュが空の状態で認証成功')

        elif cache_data == username:
            logger.debug('キャッシュに保存された内容と等しいため認証失敗')

        else:
            data['success'] = True
            data['message'] = ""
            logger.debug('cacheは' + cache_data + "で" + 'usernameは' + username + "で認証成功")

        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json')


class ValidateEmailAjaxView(View):
    """メールアドレスが既に使われているかチェック"""

    def get(self, request, *args, **kwargs):
        key = "valid_email"
        cache_data = cache.get(key)
        email = request.GET.get('email')

        data = {
            'success': False,
            'message': "このメールアドレスを持ったユーザーが既に存在します。",
        }

        # キャシュが空
        if not cache_data:
            try:
                # 入力されたメアドが存在すればキャッシュに保存
                exist_email = get_user_model().objects.filter(email__iexact=email).get().email
                cache.set(key, exist_email, CACHE_TIMEOUT)
                logger.debug('メアドをキャッシュに保存')

            except Exception:
                data['success'] = True
                data['message'] = ""
                logger.debug('キャッシュが空の状態で認証成功')

        elif cache_data == email:
            logger.debug('キャッシュに保存された内容と等しいため認証失敗')

        else:
            data['success'] = True
            data['message'] = ""
            logger.debug('cacheは' + cache_data + "で" + 'emailは' + email + "で認証成功")

        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json')

from django.views.generic import TemplateView
from social_django.models import UserSocialAuth


class AccountView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        error_message = request.GET.get("error_message")
        user = request.user
        auth = (
            UserSocialAuth.objects.get(user_id=user.id)
            if user.is_authenticated
            else None
        )

        context = {"user": request.user, "auth": auth, "error_message": error_message}

        return self.render_to_response(context=context)

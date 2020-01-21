from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


class MixinView(View):

    """ The purpose of this MixIn View is to disallow all
        unauthorized users access to a specific view.

        Extends:
            View
    """

    def dispatch(self, request, *args, **kwargs):
        """ The purpose of this method is to return a response for this
                view.
                Args:
                    args -- Contains the request, as well as some other arguments
                    kwargs -- keyword arguments
                Returns:
                    Default view response for valid/invalid login attempt
        """
        if self.request.user.is_authenticated:
            return redirect(reverse('map'))
        return super().dispatch(request, *args, **kwargs)


class RedirectView(View):
    """ The purpose of this Redirect View is to return
        127.0.0.0:8000/v1/ instead of 127.0.0.0:8000/.

            Extends:
                View
    """
    @staticmethod
    def get(self, request, *args, **kwargs):
        """ The purpose of this method is to return a response for this
                view.
                Args:
                    args -- Contains the request, as well as some other arguments
                    kwargs -- keyword arguments
                Returns:
                    Default view response for 127.0.0.0:8000/v1/
        """
        return HttpResponseRedirect(reverse('login_page'))

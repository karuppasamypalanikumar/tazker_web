from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import controllers
from rest_framework.status import (
    HTTP_200_OK
)


# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request: Request):
        signup_controller = controllers.SignUpController(
            request=request
        )
        return Response(
            data=signup_controller.display_details(),
            status=HTTP_200_OK
        )


class SignInView(APIView):
    permission_classes = [AllowAny]
    def post(self, request: Request):
        signin_controller = controllers.SignInController(
            request = request
        )
        return Response(
            data=signin_controller.display_values(),
            status=HTTP_200_OK
        )


class SignOutView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class VerifyEmailView(APIView):
    def get(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )

    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class ChangePasswordView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class DeleteAccountView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )

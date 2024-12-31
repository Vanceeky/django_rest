from django.shortcuts import render
from .serializers import NoteSerializer, UserRegistrationSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .models import Note
# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']


            res = Response()

            res.data = {'success':True}

            res.set_cookie(
                key='access_token',
                value=str(access_token),
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            res.set_cookie(
                key='refresh_token',
                value=str(refresh_token),
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            res.data.update(tokens)
            return res
        
        except Exception as e:
            print(e)
            return Response({'success':False})

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data

            access_token = tokens['access']

            res = Response()

            res.data = {"refreshed": True}

            res.set_cookie(key='access_token', value=access_token, httponly=True, secure=True, samesite='None', path='/')

            return res

        except:
            return Response({"refreshed": False})



@api_view(['POST'])
def logout(request):
    try:
        res = Response()
        res.data = {"success": True}

        res.delete_cookie('access_token', path='/', samesite='None')

        res.delete_cookie('refresh_token', path='/', samesite='None')

        return res
    except:
        return Response({"success": False})


@api_view(['POST'])
@permission_classes([IsAuthenticated]) #user must be authenticated to access this api 
def is_authenticated(request):
    return Response({"authenticated": True})


@api_view(['POST'])
@permission_classes([AllowAny])
def reqister(request):
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated]) #user must be authenticated to access this api function
def getNotes(request):
    user = request.user
    notes = Note.objects.filter(user = user)

    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data, status = status.HTTP_200_OK)







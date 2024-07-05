from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,PetSerializer,PetPhotosSerializer
from api.models import User,Pet,PetPhotos
from rest_framework import status
from django.http import Http404
import bcrypt
from django.contrib.auth import login,authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes as view_permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser



# Create your views here. Enviar token Token: ghuheguew
class User_APIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,format=None, *args, **kwargs):
        print(request.user)
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]
    @view_permissions((AllowAny,))
    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                hashed_password = bcrypt.hashpw(serializer.validated_data['password'].encode('utf-8'), bcrypt.gensalt())
                serializer.validated_data['password'] = hashed_password.decode('utf-8')
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    @csrf_exempt
    @view_permissions((AllowAny,))
    def login(request, format=None):
        try:
            mail = request.data.get('mail')
            password = request.data.get('password')

            if not mail or not password:
                return Response({"error": "Faltan credenciales"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(mail=mail)
            except User.DoesNotExist:
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            stored_password_hash = user.password

            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                print("ok")
                token, created = Token.objects.get_or_create(user=user)
                print(token)
                serializer = UserSerializer(user, many=False)
                return Response({"message": "Inicio de sesión exitoso", "user": serializer.data,"token":token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    
        
    


class Pet_APIView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    @view_permissions((AllowAny,))
    def get(self, request,format=None, *args, **kwargs):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            pet = PetSerializer(data=request.data,many=False)
            print(pet)
            if pet.is_valid():
                pet.save()
                return Response(pet.data, status=status.HTTP_201_CREATED)
            return Response(pet.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    @csrf_exempt
    @view_permissions((AllowAny,))
    def getByUser(request,id):
        print(id)
        pets = Pet.objects.filter(owner = id)
        serializer = PetSerializer(pets,many=True)
        return Response(serializer.data)


class PetPhotoUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = PetPhotosSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

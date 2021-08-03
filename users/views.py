import datetime
import jwt
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookMetaInfoSerializer
from books.views import StandardResultsSetPagination
from .models import User
from .serializers import UserSerializer


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        user_without_id = serializer.data
        response.data = user_without_id

        user = User.objects.filter(email=user_without_id['email']).first()
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response.data["token"] = token

        return response


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User Not Found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.data = {
            'token': token,
            'success': True
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.headers.get('Authentication')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.get(id=payload['id'])
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        token = request.headers.get('Authentication')

        if not token:
            raise AuthenticationFailed('Not Logged In')

        response = Response()
        response.delete_cookie('auth')
        response.data = {
            'success': True
        }
        return response


class PostLibraryView(APIView):

    def delete(self, request, pk):
        token = request.headers.get('Authentication')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.get(id=payload['id'])

        if user:
            if Book.objects.filter(book_id=pk).exists():
                book = Book.objects.get(book_id=pk)
                user.library.remove(book)
                response = Response()
                response.data = {
                    'success': True,
                    'message': 'Book Removed Successfully'
                }
                return response
            else:
                return Response({'success': False, 'message': 'Wrong Book ID'})
        else:
            raise AuthenticationFailed('Unauthenticated')

    def post(self, request, pk):
        token = request.headers.get('Authentication')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.get(id=payload['id'])
        if user:
            if Book.objects.filter(book_id=pk).exists():
                book = Book.objects.get(book_id=pk)
                user.library.add(book)
                response = Response()
                response.data = {
                    'success': True,
                    'message': 'Book Added Successfully'
                }
                return response
            else:
                return Response({'success': False, 'message': 'Wrong Book ID'})
        else:
            raise AuthenticationFailed('Unauthenticated')


class GetLibraryView(generics.ListAPIView):
    serializer_class = BookMetaInfoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ['book_id', 'isbn', 'title', 'authors', 'avg_rating', 'ratings_count']
    search_fields = ['isbn', 'title', 'genre', 'authors']

    def get_queryset(self):
        token = self.request.headers.get('Authentication')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()

        if user:
            return user.library.all()
        else:
            raise AuthenticationFailed('Unauthenticated')

from django.contrib.auth import authenticate, login
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from portfolio.api.permissions import IsOwnerOrReadOnly
from portfolio.api.serializers import UserSerializer, ProjectSerializer
from portfolio.models import User, Project


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('id', 'first_name', 'last_name', 'username')
    # /users/?search=rudy searches across all listed fields
    # search_fields = ('first_name', 'last_name', 'about')
    # /users/?ordering=first_name orders by first name alphabetically
    # ordering_fields = ('first_name', 'last_name')
    # /users/ default ordering is by the highest id
    # ordering = ('-id',)

    # lookup_field = 'username'
    @list_route()
    def recent_users(self, request):
        recent_users = User.objects.all()\
            .order_by('-last_login')
        page = self.paginate_queryset(recent_users)
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)

    @list_route()
    def my_follows(self, request):
        my_follows = request.user\
            .followed_project.all()
        page = self.paginate_queryset(my_follows)
        serializer = ProjectSerializer(page, many=True)
        return Response(serializer.data)

    @detail_route()
    def following(self, request, pk):
        my_follows = User.objects.get(pk=pk)\
            .followed_project.all()
        page = self.paginate_queryset(my_follows)
        serializer = ProjectSerializer(page, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def register(self, request):
        user = User.objects.create_user(
            username=request.DATA.get('username', None),
            password=request.DATA.get('password', None)
        )
        login(request, user)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def login(self, request):
        username = request.DATA.get('username', None)
        password = request.DATA.get('password', None)

        if username is not None and password is not None:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    token, created = Token.objects.get_or_create(user=user)
                    serializer = self.get_serializer(user)
                    return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ProjectViewSet(viewsets.ModelViewSet):
    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_fields = ('title','owner__username',)
    permission_classes = (IsOwnerOrReadOnly,)
    ordering = ('-id',)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def get_queryset(self):
        queryset = Project.objects.all()
        username = self.request.QUERY_PARAMS.get('username', None)
        if username is not None: # Optionally filters against 'username' query param
            queryset = queryset.filter(owner__username=username)
        return queryset

    @detail_route(methods=['post'])
    def follow(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.follower.add(request.user)
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['delete'])
    def unfollow(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.follower.remove(request.user)
        return Response(status=status.HTTP_200_OK)
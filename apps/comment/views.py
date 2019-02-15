from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from .models import Comment
from .filters import CommentFilter
from .serializer import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    serializer_class = CommentSerializer
    # django_filters
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


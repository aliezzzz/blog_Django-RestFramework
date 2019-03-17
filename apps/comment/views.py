from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from .models import Comment, Articles
from .filters import CommentFilter
from .serializer import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = CommentSerializer
    # django_filters
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter

    def destroy(self, request, *args, **kwargs):
        comment_id = kwargs['pk']
        print(comment_id)
        comment = Comment.objects.get(pk=comment_id)
        post_id = comment.post_id
        article = Articles.objects.get(id=post_id)
        if article.comment_count >= 0:
            article.comment_count -= 1
            print(article.comment_count)
        article.save()
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


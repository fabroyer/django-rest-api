from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from support.permissions import IsAdminAuthenticated, IsAuthorOrReadOnly
from support.models import Project, Issue, Comment, Contributor
from support.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer


# A ViewSet is tied to a specific model and handles all CRUD operations for it.
# An APIView is used for a specific action.
# Here, the queryset line does the same thing as get_queryset, but without allowing custom filtering.
class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    # Here, we allow the user to make requests for the project if they are the author OR a contributor.
    def get_queryset(self):
        print(self.request.user)
        return Project.objects.filter(Q(author = self.request.user) | Q(contributor__user = self.request.user))

    # The serializer marks `author` as read-only, but the model still requires the field.
    # This view ensures that the author is automatically set to the current authenticated user.
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Issue.objects.filter(Q(author = self.request.user) | Q(project__contributor__user = self.request.user))

    # We take the user of each project contributor
    # you must be in this user list for the view to say to the model the author is the user.
    # An issue can only be created by the author or a contributor,
    # if it can be created the user will be registered as the issue author.
    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        contributors = [contributor.user for contributor in project.contributor_set.all()]
        if self.request.user in contributors or self.request.user == project.author:
            serializer.save(author = self.request.user)
        else:
            raise PermissionDenied("Vous n'êtes pas contributeur sur ce projet.")


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def get_queryset(self):
        return Comment.objects.filter(Q(author = self.request.user) | Q(issue__project__contributor__user = self.request.user))

    def perform_create(self, serializer):
        issue = serializer.validated_data['issue']
        project = issue.project
        contributors = [contributor.user for contributor in project.contributor_set.all()]
        if self.request.user in contributors or self.request.user == project.author:
            serializer.save(author = self.request.user)
        else:
            raise PermissionDenied("Vous n'êtes pas contributeur sur ce projet.")

class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    # If we want the contributors, we will get the list of contributors
    # when the user is either the author or a contributor.
    def get_queryset(self):
        return Contributor.objects.filter(Q(project__author = self.request.user) | Q(project__contributor__user = self.request.user))

    # Only the author of a project can add a contributor to the project.
    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if project.author == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission d'ajouter cet utilisateur à ce projet.")


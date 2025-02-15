from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Project, Task
from rest_framework.exceptions import PermissionDenied
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("Authentication required.")
        
        if user.role == 'Admin':
            return User.objects.all()
        
        return User.objects.filter(id=user.id)

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.role != 'Admin' and request.user != user:
            raise PermissionDenied("You are not authorized to view this profile.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.role != 'Admin' and request.user != user:
            raise PermissionDenied("You are not authorized to update this profile.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != 'Admin':
            raise PermissionDenied("Only Admins can delete users.")
        return super().destroy(request, *args, **kwargs)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        return Project.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        if self.request.user.role != 'Admin':
            raise PermissionDenied("Only Admins can create projects.")
        
        serializer.save(creator=self.request.user)

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        if request.user.role != 'Admin' or request.user != project.creator:
            raise PermissionDenied("Only the project creator (Admin) can update this project.")
        
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if request.user.role != 'Admin' or request.user != project.creator:
            raise PermissionDenied("Only the project creator (Admin) can delete this project.")
        
        return super().destroy(request, *args, **kwargs)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        if self.request.user.role != 'Admin':
            raise PermissionDenied("Only Admins can create tasks.")

        serializer.save()

    def update(self, request, *args, **kwargs):
        task = self.get_object()

        if not request.user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        if request.user.role == "Admin":
            return super().update(request, *args, **kwargs)

        elif request.user.role == "Member":
            if "status" in request.data and len(request.data) == 1:
                task.status = request.data["status"]
                task.save()
                return Response({"message": "Task status updated successfully."})

            raise PermissionDenied("Members can only update task statuses.")

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        if request.user.role != 'Admin':
            raise PermissionDenied("Only Admins can delete tasks.")

        return super().destroy(request, *args, **kwargs)

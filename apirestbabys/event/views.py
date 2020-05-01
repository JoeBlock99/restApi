from rest_framework import viewsets
from rest_framework.response import Response
from guardian.shortcuts import assign_perm
from event.models import Event
from event.serializers import EventSerializer
from authorization.services import APIAuthorizationClassFactory


def check_child(user, obj, request):
    return user.first_name == obj.baby.parent.name


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (APIAuthorizationClassFactory(
        name='eventPermission',
        permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': check_child,
                    'destroy': check_child,
                    'update': check_child,
                    'partial_update': check_child,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        event = serializer.save()
        user = self.request.user
        assign_perm('events.change_event', user, event)
        assign_perm('events.view_event', user, event)
        return Response(serializer.data)
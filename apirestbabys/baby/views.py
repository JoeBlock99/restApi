from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from baby.models import Baby
from event.models import Event
from baby.serializers import BabySerializer
from event.serializers import EventSerializer
from guardian.shortcuts import assign_perm
from authorization.services import APIPermissionClassFactory
# Create your views here.


def parent_check(user, obj, request):
    return user.username == obj.parent.name


class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': parent_check,
                    'destroy': parent_check,
                    'update': parent_check,
                    'partial_update': parent_check,
                    'events': parent_check,
                    # 'update_permissions': 'users.add_permissions'
                    # 'archive_all_students': phase_user_belongs_to_school,
                    # 'add_clients': True,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.change_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, url_path='events', methods=['get'])
    def events(self, request, pk=None):
        allEvents = Event.objects.all().filter(baby=pk)
        return Response(EventSerializer(allEvents, many=True).data)
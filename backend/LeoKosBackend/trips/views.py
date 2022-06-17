from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Trip
from .serializers.common import TripSerializer

class TripListView(APIView):

    def get(self, _request):
        trips = Trip.objects.all()
        serialized_trips = TripSerializer(trips, many=True)
        return Response(serialized_trips.data, status=status.HTTP_200_OK)

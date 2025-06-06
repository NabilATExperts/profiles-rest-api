from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional DJango view',
            'Gives you the most control over your application logic'
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})
from rest_framework.views import APIView
from rest_framework.response import response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of api views feature"""

        an_apiview = [
             'Uses HTTP as function (get, post, put , delete)',
             'Is Similar to a traditional Django View',
             'Gives you most control over your application logic ',
             'Is mapped manually to urls',
        ]

        return response({'message':'Hello!','an_apiview': an_apiview})
# Create your views here.


from api.models import Contact
from api.serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# @api_view(['PUT'])
# def post_detail(request, pk):
# try:
#     print(pk)
#     res = Contact.objects.get(id=pk)
#     except Contact.DoesNotExist:
#     return Response('Contact list not found', status=404)
#     if(request.method == 'PUT'):
#         ser = PostSerializer(instance=res, data=request.data)
#         if(ser.is_valid()):
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response('some error occured')


# @api_view(['PUT'])
# def like(request, pk):
#     try:
#         res = Post.objects.get(id=pk)
#     except Post.DoesNotExist:
#         return Response('Post list not found', status=404)
#     res.like_count += 1
#     res.save()
#     return Response('OK')


class ContactView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ) # for identify a user
    # def get(self, request):
    #     #posts = Post.objects.all()
    #     posts = Post.objects.for_user(created_by = self.request.user)
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        #return Post.objects.all()
        return Contact.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return ContactSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


    # def post(self, request):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

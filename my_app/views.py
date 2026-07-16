from my_app.models import * 
from my_app.serializer import * 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def student_view(req):
    if req.method == 'GET':
        student_data = studentModel.objects.all()
        serializer_data = studentSerializer(student_data, many=True)
        return Response({
            "success" : True,
            "message": "Student Data get Successfully.",
            "data": serializer_data.data
        })

    if req.method =='POST':
        serializer_data = studentSerializer(data = req.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                "success" : True,
                "message": "Student Data POST Successfully.",
                "data": serializer_data.data
            })
        return Response({
            "success": False,
            "message":"Invalid",
            "data": serializer_data.errors
        })



#  subject

@api_view(['GET','POST'])
def subject_view(req):
    if req.method == 'GET':
        subject_Data = subjectModel.objects.all()
        serializer_Data = subjectSerializer(subject_Data, many=True)
        return Response({
            "success":True,
            "message": "Successfully Get Subject",
            "data":serializer_Data.data
        })
    if req.method == 'POST':
        serializer_Data = subjectSerializer(data = req.data)
        if serializer_Data.is_valid():
            serializer_Data.save()
            return Response({
                "success":True,
                "message": "Successfully created Subject",
                "data":serializer_Data.data
            })
        return Response({
            "success":True,
            "message": "Invalid Subject",
            "data":serializer_Data.errors
        })



   # ----------------------------->certain get<---------------------------------
@api_view(['GET','PUT','DELETE'])
def subject_detail(req, id):

    try:
        subject_data = subjectModel.objects.get(id = id)
    except:
        
        return Response({
            "success":False,
            "message":"Data No found !",     
        },status= status.HTTP_404_NOT_FOUND)


    if req.method == 'GET':
        serializers_Data = subjectSerializer(subject_data)
        return Response({
            "success":True,
            "message":"Successfully Get update",
            "data":serializers_Data.data
        })
    

    # ----------------------------->delete<---------------------------------

    elif req.method == 'DELETE':
        subject_data.delete()
        return Response({
            "success":True,
            "message":"Successfully delete successfully",
        })
    
    elif req.method == 'PUT':
        serializers_Data = subjectSerializer(subject_data, data=req.data)
        if serializers_Data.is_valid():
            serializers_Data.save()
        return Response({
            "success":True,
            "message":"Successfully update",
            "data":serializers_Data.data
        })
    else:
        return Response({
            "success":False,
            "message":serializers_Data.errors, 
        }, status = status.HTTP_204_NO_CONTENT)

    

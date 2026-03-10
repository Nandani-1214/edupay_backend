from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.http import JsonResponse
#add-money
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *

from rest_framework import status
@api_view(['POST'])
def admin_login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        admin = Admin.objects.get(email=email)

        if admin.password == password:
            return Response({
                "message": "Login successful",
                "email": admin.email,
                "admin_id": admin.id
            })

        else:
            return Response({"error": "Invalid password"}, status=400)

    except Admin.DoesNotExist:
        return Response({"error": "Email not found"}, status=404)
#student
# GET ALL STUDENTS
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all().order_by('-id')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# ADD STUDENT
@api_view(['POST'])
def add_student(request):
    print("REQUEST DATA:", request.data)   # ADD THIS
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student Added Successfully"}, status=status.HTTP_201_CREATED)

    print("SERIALIZER ERRORS:", serializer.errors)   # ADD THIS
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UPDATE STUDENT
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student Updated Successfully"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE STUDENT
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({"message": "Student Deleted Successfully"})
    
#vendor module 
# GET ALL VENDORS
# ===============================
@api_view(['GET'])
def get_vendors(request):
    vendors = Vendor.objects.all().order_by('-id')
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)


# ===============================
# ADD VENDOR
# ===============================
@api_view(['POST'])
def add_vendor(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Vendor Added Successfully"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===============================
# UPDATE VENDOR
# ===============================
@api_view(['PUT'])
def update_vendor(request, id):
    try:
        vendor = Vendor.objects.get(id=id)
    except Vendor.DoesNotExist:
        return Response(
            {"error": "Vendor Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = VendorSerializer(vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Vendor Updated Successfully"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===============================
# DELETE VENDOR
# ===============================
@api_view(['DELETE'])
def delete_vendor(request, id):
    try:
        vendor = Vendor.objects.get(id=id)
    except Vendor.DoesNotExist:
        return Response(
            {"error": "Vendor Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    vendor.delete()
    return Response({"message": "Vendor Deleted Successfully"})

#parent 
# GET ALL PARENTS
@api_view(['GET'])
def get_parents(request):
    parents = Parent.objects.all().order_by('-id')
    serializer = ParentSerializer(parents, many=True)
    return Response(serializer.data)

# ADD PARENT
@api_view(['POST'])
def add_parent(request):
    try:
        print ('in')
        roll = request.data.get("studentRoll")
        print("roll==>",roll)

        # if not roll:
        #     print ("not rle")
        #     return Response({"error": "Student Roll Number required"}, status=400)

        student = Student.objects.get(roll=roll)
        print('student==>',student)
        
        parent = Parent.objects.create(
            student=student,
            name=request.data.get("name"),
            email=request.data.get("email"),
            relation=request.data.get("relation"),
            address=request.data.get("address"),
            # roll_number = parent.student_roll_no,
            phone=student.phone  # AUTO COPY FROM STUDENT
        )
        print("parent==>",parent)

        return Response({"message": "Parent Added Successfully"}, status=201)

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    except Exception as e:
        return Response({"error": str(e)}, status=400)


# DELETE
@api_view(['DELETE'])
def delete_parent(request, id):
    try:
        parent = Parent.objects.get(id=id)
        parent.delete()
        return Response({"message": "Deleted successfully"})
    except Parent.DoesNotExist:
        return Response({"error": "Parent not found"}, status=404)
    


@csrf_exempt
def check_parent_email(request):

    if request.method == "POST":

        data = json.loads(request.body)
        email = data.get("email")

        try:
            parent = Parent.objects.get(email=email)

            return JsonResponse({
                "status": "success",
                "message": "Parent Found",
                "parent_id": parent.id,
                "email": parent.email
            })

        except Parent.DoesNotExist:

            return JsonResponse({
                "status": "error",
                "message": "Parent is not registered"
            })

    return JsonResponse({
        "status": "error",
        "message": "Invalid request"
    })


@csrf_exempt
def get_student_details(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")

            parent = Parent.objects.get(email=email)
            student = parent.student

            return JsonResponse({
                "status": "success",
                "name": student.name,
                "class": student.student_class,
                "division": student.division,
                "roll": student.roll,
                "phone": student.phone,
                "rfid": student.rfid
            })

        except Parent.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Parent not found"
            })

    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    })




@csrf_exempt
def add_money(request):

    if request.method == "POST":

        data = json.loads(request.body)

        email = data.get("email")
        amount = data.get("amount")

        try:
            parent = Parent.objects.get(email=email)

        except Parent.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Parent not found"
            })

        student_id = parent.student_id

        try:
            student = Student.objects.get(id=student_id)

        except Student.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Student not found"
            })

        wallet, created = Wallet.objects.get_or_create(student=student)

        wallet.balance += float(amount)
        wallet.save()

        Transaction.objects.create(
            student=student,
            amount=amount
        )

        return JsonResponse({
            "status": "success",
            "message": "Money added successfully",
            "new_balance": wallet.balance
        })

    return JsonResponse({
        "status": "error",
        "message": "POST request required"
    })
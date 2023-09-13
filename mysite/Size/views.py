from  django.shortcuts import render,redirect
from Size.models import Size
from django.contrib import messages
from Size.serializers import SizeSerializer,SIZESerializer

def show_size(request):
    showsize = Size.objects.filter(isactive=True)
    print(showsize)
    serializer = SizeSerializer(showsize,many=True)
    print(serializer.data)
    return render(request,'polls/show_size.html',{"data":serializer.data})

def insert_size(request):
    if request.method == "POST":
        # if request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('department') and request.POST.get('designation') and request.POST.get('location') and request.POST.get('status') and request.POST.get('salary') and request.POST.get('gender'):
        #     saverecord = EmpModel()
        #     saverecord.firstname = request.POST.get('firstname')
        #     saverecord.middlename = request.POST.get('middlename')
        #     saverecord.lastname = request.POST.get('lastname')
        #     saverecord.location = request.POST.get('location')
        #     saverecord.designation = request.POST.get('designation')
        #     saverecord.department = request.POST.get('department')
        #     saverecord.status = request.POST.get('status')
        #     saverecord.salary = request.POST.get('salary')
        #     saverecord.gender = request.POST.get('gender')
        #     saverecord.save()
        #     messages.success(request,'Employee ' + saverecord.firstname + ' is saved successfully :)!')
        #     return render(request,'Insert.html')
        insertsize = {}
        insertsize['size_name']=request.POST.get('size_name')
        insertsize['size_description']=request.POST.get('size_description')
        form = SizeSerializer(data=insertsize)
        if form.is_valid():
            form.save()
            print("hkjk",form.data)
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('Size:show_size')
        else:
            print(form.errors)
    else:
            return render(request,'polls/insert_size.html')


def edit_size(request,id):
    if request.method == 'GET':
        print('GET',id)
        editsize = Size.objects.filter(id=id).first()
        s= SizeSerializer(editsize)
        return render(request,'polls/edit_size.html',{"Size":s.data})
    else:
        print('POST',id)
        editsize = {}
        
        d = Size.objects.filter(id=id).first()
        if d:
            editsize['size_name']=request.POST.get('size_name')
            editsize['size_description']=request.POST.get('size_description')
            print(editsize)
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = SizeSerializer(d,data=editsize)
            if form.is_valid():
                form.save()
                print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('Size:show_size')
            else:
                print(form.errors)
    



# def updateemp(request,id):
#     # Updateemp = {}
#     # if request.method=='POST':
#     #     data = EmpModel.objects.get(id=id)
#     #     if data:
#     #         Updateemp['firstname']=request.POST.get('firstname')
#     #         Updateemp['middlename']=request.POST.get('middlename')
#     #         Updateemp['lastname']=request.POST.get('lastname')
#     #         Updateemp['department']=request.POST.get('department')
#     #         Updateemp['designation']=request.POST.get('designation')
#     #         Updateemp['status']=request.POST.get('status')
#     #         Updateemp['salary']=request.POST.get('salary')
#     #         Updateemp['gender']=request.POST.get('gender')
#     #     # Updateemp = EmpModel.objects.get(id=id)
#     #         #print(Updateemp)
#     #         form = CRUDSerializer(data,data=Updateemp)
#     #         if form.is_valid():
#     #             form.save()
#     #             messages.success(request,'Record Updated Successfully...!:)')
#     #             return render(request,'Edit.html',{"EmpModel":Updateemp})
#     # return render(request,'Edit.html',Updateemp)


def delete_size(request,id):
    deletecolors = Size.objects.get(id=id)
    delsize={}
    delsize['isactive']=False
    form = SIZESerializer(deletecolors,data=delsize)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Deleted Successfully...!:)')
        return redirect('Size:show_size')
    else:
        print("sfsdrf",form.errors)
        return redirect('Size:show_size')
    

from  django.shortcuts import render,redirect
from colors.models import Colors
from django.contrib import messages
from .serializers import ColorsSerializer,COLORSSerializer

def show_colors(request):
    showcolors = Colors.objects.filter(isactive=True)
    print(showcolors)
    serializer = ColorsSerializer(showcolors,many=True)
    print(serializer.data)
    return render(request,'polls/show_colors.html',{"data":serializer.data})

def insert_colors(request):
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
        insertcolors = {}
        insertcolors['color_name']=request.POST.get('color_name')
        insertcolors['color_description']=request.POST.get('color_description')
        form = ColorsSerializer(data=insertcolors)
        if form.is_valid():
            form.save()
            print("hkjk",form.data)
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('colors:show_colors')
        else:
            print(form.errors)
            return redirect('colors:show_colors')
    else:
        insertcolors = {}
        form = ColorsSerializer(data=insertcolors)  
        if form.is_valid(): 
            print(form.errors)   
        return render(request,'polls/insert_colors.html')


def edit_colors(request,id):
    if request.method == 'GET':
        print('GET',id)
        editcolors = Colors.objects.filter(id=id).first()
        s= ColorsSerializer(editcolors)
        return render(request,'polls/edit_colors.html',{"Colors":s.data})
    else:
        print('POST',id)
        editcolors = {}
        
        d = Colors.objects.filter(id=id).first()
        if d:
            editcolors['color_name']=request.POST.get('color_name')
            editcolors['color_description']=request.POST.get('color_description')
            print(editcolors)
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = ColorsSerializer(d,data=editcolors)
            if form.is_valid():
                form.save()
                print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('colors:show_colors')
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


def delete_colors(request,id):
    deletecolors = Colors.objects.get(id=id)
    delcolors={}
    delcolors['isactive']=False
    form = COLORSSerializer(deletecolors,data=delcolors)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Deleted Successfully...!:)')
        return redirect('colors:show_colors')
    else:
        print("sfsdrf",form.errors)
        return redirect('colors:show_colors')
    

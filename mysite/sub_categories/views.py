from django import forms
from  django.shortcuts import render,redirect
from sub_categories.models import SUBCategories
from django.contrib import messages
from sub_categories.serializers import  SUBCategoriesSerializer,subCategoriesSerializer
from categories.serializers import CategoriesSerializer
from categories.models import Categories

def show_sub_categories(request):
    showsubcategories = SUBCategories.objects.filter(isactive=True)
    #print(showsubcategories)
    serializer = SUBCategoriesSerializer(showsubcategories,many=True)
    print(serializer.data)
    return render(request,'polls/show_sub_categories.html',{"results":serializer.data})

def insert_sub_categories(request):
    if request.method == "POST":
        form = SUBCategoriesSerializer(data=request.POST)        
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('sub_categories:show_sub_categories')
        else:
            print(form.errors)

    else:
        form = SUBCategoriesSerializer()
        category_dict = Categories.objects.filter(isactive=True)
        category = CategoriesSerializer(category_dict,many=True)
        hm = {'context': category.data, 'form':form}
    return render(request,'polls/insert_sub_categories.html',hm)

def edit_sub_categories(request,id):
    if request.method == 'GET':
        print('GET',id)
        editsubcategories = SUBCategories.objects.filter(id=id).first()
        s= SUBCategoriesSerializer(editsubcategories)
        return render(request,'polls/edit_sub_categories.html',{"SUBCategories":s.data})
    else:
        print('POST',id)
        editsubcategories = {}
        
        d = SUBCategories.objects.filter(id=id).first()
        if d:
            editsubcategories['sub_categories_name']=request.POST.get('sub_categories_name')
            editsubcategories['sub_categories_description']=request.POST.get('sub_categories_description')
            print(editsubcategories)
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = SUBCategoriesSerializer(d,data=editsubcategories)
            if form.is_valid():
                form.save()
                print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('sub_categories:show_sub_categories')
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


def delete_sub_categories(request,id):
    deletesubcategories = SUBCategories.objects.get(id=id)
    delsubcategories={}
    delsubcategories['isactive']=False
    form = subCategoriesSerializer(deletesubcategories,data=delsubcategories)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Deleted Successfully...!:)')
        return redirect('sub_categories:show_sub_categories')
    else:
        print("sfsdrf",form.errors)
        return redirect('sub_categories:show_sub_categories')
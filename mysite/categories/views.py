from  django.shortcuts import render,redirect
from categories.models import Categories
from django.contrib import messages
from categories.serializers import CategoriesSerializer,CATEGORIESSerializer

def show_cat(request):
    showcategory = Categories.objects.filter(isactive=True)
    #print(showall)
    serializer = CategoriesSerializer(showcategory,many=True)
    #print(serializer.data)
    return render(request,'polls/show_cat.html',{"data":serializer.data})

def insert_cat(request):
    if request.method == "POST":
        insertcategory = {}
        insertcategory['category_name.id']=request.POST.get('category_name')
        insertcategory['category_description']=request.POST.get('category_description')
        form = CategoriesSerializer(data=insertcategory)
        if form.is_valid():
            form.save()
            print("hkjk",form.data)
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('categories:show_cat')
        else:
            print(form.errors)
            return redirect('categories:show_cat')
    else: 
        return render(request,'polls/insert_cat.html')


def edit_cat(request,id):
    if request.method == 'GET':
        print('GET',id)
        editcategory = Categories.objects.filter(id=id).first()
        s= CategoriesSerializer(editcategory)
        return render(request,'polls/edit_cat.html',{"Categories":s.data})
    else:
        print('POST',id)
        editcategory = {}
        
        d = Categories.objects.filter(id=id).first()
        if d:
            editcategory['category_name']=request.POST.get('category_name')
            editcategory['category_description']=request.POST.get('category_description')
            print(editcategory)
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = CategoriesSerializer(d,data=editcategory)
            if form.is_valid():
                form.save()
                print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('categories:show_cat')
            else:
                print(form.errors)
    


def del_cat(request,id):
    delcategory = Categories.objects.get(id=id)
    delcat={}
    delcat['isactive']=False
    form = CATEGORIESSerializer(delcategory,data=delcat)
    if form.is_valid():
        print(form.errors)
        form.save()
        messages.success(request,'Record Deleted Successfully...!:)')
        return redirect('categories:show_cat')
    else:
        print("sfsdrf",form.errors)
        return redirect('categories:show_cat')
    

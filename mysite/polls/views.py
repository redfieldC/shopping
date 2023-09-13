from  django.shortcuts import render,redirect
from polls.models import Products
from django.contrib import messages
from polls.serializers import POLLSerializer

def showemp(request):
    showall = Products.objects.all()
    print(showall)
    serializer = POLLSerializer(showall,many=True)
    print(serializer.data)
    return render(request,'polls/starter.html',{"data":serializer.data})

def show(request):
    showall = Products.objects.all()
    print(showall)
    serializer = POLLSerializer(showall,many=True)
    print(serializer.data)
    return render(request,'polls/product_list.html',{"data":serializer.data})


def Insertemp(request):
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
        Updateemp = {}
        Updateemp['Categories']=request.POST.get('Categories')
        Updateemp['sub_categories']=request.POST.get('sub_categories')
        Updateemp['lastname']=request.POST.get('lastname')
        Updateemp['Color']=request.POST.get('Color')
        Updateemp['Size']=request.POST.get('Size')
        Updateemp['image']=request.POST.get('image')
        Updateemp['title']=request.POST.get('title')
        Updateemp['sku_number']=request.POST.get('sku_number')
        Updateemp['prod_details']=request.POST.get('prod_details')
        Updateemp['quantity']=request.POST.get('quantity')
        form = POLLSerializer(data=Updateemp)
        if form.is_valid():
            form.save()
            print("hkjk",form.data)
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('app1:showemp')
        else:
            print(form.errors)
    else:
            return render(request,'Insert.html')

#insert detail
def insert(request):
    if request.POST == "POST":
        insert_clothes = {}
        insert_clothes['Categories']=request.POST.get('Categories')
        insert_clothes['sub_categories']=request.POST.get('sub_categories')
        insert_clothes['lastname']=request.POST.get('lastname')
        insert_clothes['Color']=request.POST.get('Color')
        insert_clothes['Size']=request.POST.get('Size')
        insert_clothes['image']=request.POST.get('image')
        insert_clothes['title']=request.POST.get('title')
        insert_clothes['sku_number']=request.POST.get('sku_number')
        insert_clothes['prod_details']=request.POST.get('prod_details')
        insert_clothes['quantity']=request.POST.get('quantity')
        form = POLLSerializer(data = insert_clothes)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated successfully :)!!!!')
            return redirect('polls:show')
        else:
            print(form.errors)
    else:
        return render(request,'polls/product_insert.html')
 

def Editemp(request,id):
    if request.method == 'GET':
        print('GET',id)
        editempobj = Products.objects.filter(id=id).first()
        s= POLLSerializer(editempobj)
        return render(request,'Edit.html',{"EmpModel":s.data})
    else:
        print('POST',id)
        Updateemp = {}
        
        d = Products.objects.filter(id=id).first()
        if d:
            Updateemp['Categories']=request.POST.get('Categories')
            Updateemp['sub_categories']=request.POST.get('sub_categories')
            Updateemp['lastname']=request.POST.get('lastname')
            Updateemp['Color']=request.POST.get('Color')
            Updateemp['Size']=request.POST.get('Size')
            Updateemp['image']=request.POST.get('image')
            Updateemp['title']=request.POST.get('title')
            Updateemp['sku_number']=request.POST.get('sku_number')
            Updateemp['prod_details']=request.POST.get('prod_details')
            Updateemp['quantity']=request.POST.get('quantity')
            print(Updateemp)
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = POLLSerializer(d,data=Updateemp)
            if form.is_valid():
                form.save()
                print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('app1:showemp')
            else:
                print(form.errors)
                
#update clothes information

def update(request,id):
    if request.method == 'GET':
        print('GET',id)
        edit_clothes = Products.objects.filter(id=id).first()
        s= POLLSerializer(edit_clothes)
        return render(request,'polls/product_edit.html',{"Products":s.data})
    else:
        print('POST',id)
        update_clothes = {}
        
        d = Products.objects.filter(id=id).first()
        if d:
            update_clothes['Categories']=request.POST.get('Categories')
            update_clothes['sub_categories']=request.POST.get('sub_categories')
            update_clothes['lastname']=request.POST.get('lastname')
            update_clothes['Color']=request.POST.get('Color')
            update_clothes['Size']=request.POST.get('Size')
            update_clothes['image']=request.POST.get('image')
            update_clothes['title']=request.POST.get('title')
            update_clothes['sku_number']=request.POST.get('sku_number')
            update_clothes['prod_details']=request.POST.get('prod_details')
            update_clothes['quantity']=request.POST.get('quantity')
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = POLLSerializer(d,data=update_clothes)
            if form.is_valid():
                form.save()
                # print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('polls:showemp')
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


def Delemp(request,id):
    delemployee = Products.objects.get(id=id)
    Delemp={}
    #Delemp['isactive']=False
    form = POLLSerializer(delemployee,data=Delemp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Deleted Successfully...!:)')
        return redirect('app1:showemp')
    else:
        print("sfsdrf",form.errors)
        return redirect('app1:showemp')
    


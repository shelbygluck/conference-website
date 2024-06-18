
def a9(request):
    if request.user.is_authenticated:
        return render(request,"Lab/A9/a9.html")
    else:
        return redirect('login')
@csrf_exempt
def a9_lab(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            return render(request,"Lab/A9/a9_lab.html")
        else:

            try :
                file=request.FILES["file"]
                try :
                    data = yaml.load(file,yaml.Loader)
                    
                    return render(request,"Lab/A9/a9_lab.html",{"data":data})
                except:
                    return render(request, "Lab/A9/a9_lab.html", {"data": "Error"})

            except:
                return render(request, "Lab/A9/a9_lab.html", {"data":"Please Upload a Yaml file."})
    else:
        return redirect('login')
def get_version(request):
      return render(request,"Lab/A9/a9_lab.html",{"version":"pyyaml v5.1"})



@csrf_exempt
def cmd_lab2(request):
    if request.user.is_authenticated:
        if (request.method=="POST"):
            val=request.POST.get('val')
            
            print(val)
            try:
                output = eval(val)
            except:
                output = "Something went wrong"
                return render(request,'Lab/CMD/cmd_lab2.html',{"output":output})
            print("Output = ", output)
            return render(request,'Lab/CMD/cmd_lab2.html',{"output":output})
        else:
            return render(request, 'Lab/CMD/cmd_lab2.html')
    else:
        return redirect('login')

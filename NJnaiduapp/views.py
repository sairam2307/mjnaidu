from django.shortcuts import render,redirect
from NJnaiduapp.forms import ChairmanForm 
from NJnaiduapp.models import *
def index(request):
    return render(request, 'index.html',{})
def our_hospital(request):
    return render(request, 'our-hospital.html',{})

def chairman_create(request):
    form = ChairmanForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('chairman_create')
    return render(request,'chairman_create.html', {'form':form})


def chairman(request):
    book= Chairman.objects.get(id=2)  
    return render(request, 'chairman.html', {'object':book})

def chairman_update(request, pk):
    book= get_object_or_404(Chairman, pk=pk)
    form = ChairmanForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('chairman_view')
    return render(request,'chairman_create.html', {'form':form})

# def chairman_delete(request, pk):
#     book= get_object_or_404(Book, pk=pk)    
#     if request.method=='POST':
#         book.delete()
#         return redirect('chairman_view')
#     return render(request, template_name, {'object':book})



# def chairman(request):
#     return render(request, 'chairman.html',{})
def our_team(request):
    return render(request, 'our-team.html',{})
def testimonial(request):
    return render(request, 'testimonial.html',{})
def arthoplasty(request):
    return render(request, 'arthoplasty.html',{})
def htp_replacement(request):
    return render(request, 'htp-replacement.html',{})
def knee_replacement(request):
    return render(request, 'knee-replacement.html',{})
def arthoscopy(request):
    return render(request, 'arthoscopy.html',{})
def orthopaedics(request):
    return render(request, 'orthopaedics.html',{})
def arthritis(request):
    return render(request, 'arthritis.html',{})
def bonetumours(request):
    return render(request, 'bonetumours.html',{})
def illizarov(request):
    return render(request, 'illizarov.html',{})
def orthosuv(request):
    return render(request, 'orthosuv.html',{})
def osteoporosis(request):
    return render(request, 'osteoporosis.html',{})
def paediatric(request):
    return render(request, 'paediatric.html',{})
def trauma(request):
    return render(request, 'trauma.html',{})
def spine(request):
    return render(request, 'spine.html',{})
def radiology(request):
    return render(request, 'radiology.html',{})
def painmanagement(request):
    return render(request, 'painmanagement.html',{})
def physiotheraphy(request):
    return render(request, 'physiotheraphy.html',{})
def success_stories(request):
    return render(request, 'success-stories.html',{})
def empanelment(request):
    return render(request, 'empanelment.html',{})
def ehs_ntr(request):
    return render(request, 'ehs-ntr.html',{})
def acl_rehab(request):
    return render(request, 'acl-rehab.html',{})
def packages(request):
    return render(request, 'packages.html',{})
def gallery(request):
    return render(request, 'gallery.html',{})
def contact(request):
    return render(request, 'contact.html',{})
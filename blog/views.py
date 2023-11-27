
from django.shortcuts import render,get_object_or_404,redirect

from django.views.generic import ListView

from .models import Product,Comment,Gallery

from .forms import EmailShare,CommentForm

from django.views.decorators.http import require_POST

from django.core.mail import send_mail



def index_list(request):

    product = Product.published.all()



    return render(request,'weld/welder/index.html',{'products':product})



def gallery_image(request,product):

    image = Gallery.objects.filter(product=product)

    return render(request,'weld/welder/index.html',{'image':image})








class IndexHome(ListView):

    queryset = Product.published.all()

    paginate_by = 3

    context_object_name = 'products'

    template_name = 'weld/welder/index.html'



def detail(request,year,month,day,product):

    details = get_object_or_404(Product,
                                status=Product.Status.PUBLISHED,
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,
                                slug=product)
    

    return render(request,'weld/welder/detail.html',{'details':details})



def product_share(request,product_id):
    
    product = get_object_or_404(Product,
                                id=product_id,
                                status=Product.Status.PUBLISHED)
    
    sent = False
    
    if request.method=='POST':

        form = EmailShare(request.POST) 

        if form.is_valid():

            cd = form.cleaned_data

            product_url = request.build_absolute_uri(product.get_absolute_url())

            message = f"{cd['name']} reccomends you read {product.title}"

            subject = f"Read {product.title} at {product_url}\n\n"
            f"comments {cd['name']}: {cd['comments']}"

            send_mail(subject,
                      message,
                      'kaznacheev724@gmail.com',
                      [cd['to']])
            
            sent = True


    else:

        form = EmailShare()


    return render(request,'weld/welder/share.html',{'form':form,
                                                    'sent':sent,
                                                    'product':product})






@require_POST
def comment_product(request,product_id):

    product = get_object_or_404(Product,
                                id=product_id,
                                status=Product.Status.PUBLISHED)
    
    comment = None
    
    form = CommentForm(data=request.POST)

    if form.is_valid():

        comment = form.save(commit=False)

        comment.product = product

        comment.save()

    return render(request,'weld/welder/comment.html')



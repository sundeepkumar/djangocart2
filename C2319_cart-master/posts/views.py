from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView, DetailView
from home.models import Item
from .models import Post
from django.core.mail import send_mail
from django.conf import settings
from .filters import PostFilter
from django.contrib import messages
from home.views import (remove_from_cart,
             add_to_cart,ProductView, HomeView
                    )


# Create your views here.
def add_post(request):

    if request.method == "POST":
        # form = PostForm(request.POST)
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid() :
            post_item = form.save(commit=False)
            # a = post_item.save()
            n = form.cleaned_data["title"]
            m = form.cleaned_data["cover"]
            a = form.cleaned_data["category"]
            b = form.cleaned_data["condition"]
            c = form.cleaned_data["price"]
            d = form.cleaned_data["body"]
            e = form.cleaned_data["publish"]
            t = Post(title=n, body=d , price=c, condition=b , category=a, cover=m, publish=e)
            i = Item(item_name=n, body=d , price=c, condition=b , category=a, cover=m, post = t)
            t.save()
            i.save()
            request.user.post.add(t)
            messages.success(request, 'Your new item was created successfully!', extra_tags='add')
            return redirect('/post/')
    else:
        form = PostForm()
    return render (request, '../templates/post_form.html' , {'form' : form})


class PostDetailView(DetailView):
        model = Post
        template_name = '../templates/post_detail.html'

class PostListView(ListView):
    model = Post
    template_name = '../templates/post_list.html'


class ForSaleListView(ListView):
    model = Post
    template_name = '../templates/forsale.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET , queryset = self.get_queryset())
        return context


def edit_post(request , pk=None):
    item = get_object_or_404(Post , pk=pk)
    form = PostForm(request.POST or None , request.FILES or None ,instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your item was successfully updated!', extra_tags='edit')
        return redirect('/post/' + str(pk) + '/')
    #return render (request, 'post/post_form.html' , {'form' : form})
    return render (request, '../templates/post_form.html' , {'form' : form})

def delete_post(request, pk=None):
    item = get_object_or_404(Post , pk=pk)
    form = PostForm(request.POST or None , instance=item)
    item.delete()
    messages.error(request, 'Your item was successfully deleted!', extra_tags='delete')
    return redirect('/post/')
    # return render (request, '../templates/post_list.html' , {'form' : form})


#def delete_post(request, pk=None):
#    item = get_object_or_404(Post , pk=pk)
#    form = PostForm(request.POST or None , instance=item)
#    if request.method == "POST":
#        item.delete()
#        return redirect('/post/')
#    context = { 'item' : item}
#    return render (request, '../templates/post_list.html' , context)

#**    
def contact_p(request, pk=None):
    item = get_object_or_404(Post , pk=pk)
    post_e = post.pk
    if request.method == "POST":
        message_e = request.POST['message']
        message = 'h'
        send_mail(
          'A new message from a futre buyer',
          message,
          settings.EMAIL_HOST_USER, 
          [request.user.email],
          fail_silently = False)
    return redirect('/post/')

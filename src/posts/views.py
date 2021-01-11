from django.db.models import Count, Q
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, NewsLetterRecipients
from .forms import NewsLetterForm, CommentForm



def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter( Q(title__icontains=query) | Q(overview__icontains=query)).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)


def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))

    return queryset

def index(request):
    featured = Post.objects.filter(featured = True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('index')

        else:
            form = NewsLetterForm()

    # if request.method == "POST":
    #     email = request.POST["email"]
    #     new_signup = Signup()
    #     new_signup.email = email
    #     new_signup.save()

    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)

def blog(request):
    category_count = get_category_count()
    print(category_count)
    latest_post = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page' 
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'latest_post': latest_post,
        'page_request_var': page_request_var,
        'category_count': category_count

    }
    return render(request, 'blog.html', context)

def post(request, id):
    category_count = get_category_count()
    latest_post = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id = id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post_details", kwargs = {'id': post.id}))
    context = {
        'form': form,
        'post': post,
        'latest_post': latest_post,
        'category_count': category_count
    }
    return render(request, 'post.html', context)

def post_create(request):
    pass

def post_delete(request, id):
    pass

def post_update(request, id):
    pass

def post_delete(request, id):
    pass

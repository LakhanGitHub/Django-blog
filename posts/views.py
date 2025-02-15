from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Post, Tag, User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from . forms import CommentForm
from django.db.models import Q
# Create your views here.

#creta dummy data

posts = [
    {
    'id' : 1,
    'title' : "Lets explor python",
    'content' : "Python was developed by Guido van Rossum in the early 1990s and its latest version is 3.11.0, we can simply call it Python3. Python 3.0 was released in 2008. and is interpreted language i.e it’s not compiled and the interpreter will check the code line by line. This article can be used to learn the very basics of Python programming language ."
    },
    {
    'id' : 2,
    'title' : 'Python 3 Basics',
    'content' : 'Python 3 is a popular high-level programming language used for a wide variety of applications. Here are some basics of Python 3 that you should know:'
    },
    {
    'id' : 3,
    'title' : 'Advantages of Python 3',
    'content' : 'Python 3 is a high-level language that has a large standard library and many third-party libraries available, making it a versatile language that can be used for a wide variety of applications'
    }
]


def home(request):
    all_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(all_posts,4)
    page_number = request.GET.get('p',1)
    post_obj = paginator.get_page(page_number) #read page by get requet by user
        #print(post_obj)   


    http = ''
    for post in  posts:
        http += f'''
        <div>
        <a href = '/post/{post['id']}'
        <h1>{post['id']} - {post['title']}</h1></a>
        <p>{post['content']}</p>
        </div>
        '''

    return render(request, 'posts/index.html', {"posts":post_obj})

def post(request, id):
    #try:
        #post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
             comment = form.save(commit=False)
             comment.post = post
             comment.user = request.user
             comment.save()
             posturl = reverse('post', args=[id])
             return HttpResponseRedirect(posturl)
    #valid_id = False
    #for post in posts:  
    #    if post['id'] == id:
    #        post_dict = post
    #        valid_id = True
    #        break
    #if valid_id:
        #http = f'''
         #   <h1>{post_dict['id']} - {post_dict['title']}</h1>
         #   <p>{post_dict['content']}</p>
    #except:
    #     return Http404()    #'''
    form = CommentForm()
    return render(request, 'posts/post.html', {"post_dict":post,'form':form, 'comments':post.comment_set.all()})
    #else:
    #    raise Http404()

def google(request, id):
        print(reverse('post', args=[id])) #check name and id
        url = reverse('post', args=[id])
        return HttpResponseRedirect(url)


def global1(request):
     return render(request, 'global.html')

def tag(request, id):
     tags = Tag.objects.get(id=id)
     return render(request,'posts/tag.html', {'tags':tags.post_set.all()})

def search(request):
     query = request.GET.get('query',None)
     page_number = request.GET.get('p',1)
     posts = Post.objects.filter(Q(post_title__icontains=query) | Q(post_content__icontains=query)).order_by('-id')
     paginator = Paginator(posts,4)
     page_obj = paginator.get_page(page_number)
     return render(request, 'posts/search.html',{'posts':page_obj,'query':query})
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

posts = [
    {
        "id": 0,
        "title": 'testing dynamic urls on django',
        "content": 'its working......'
    },
    {
        "id": 1,
        "title": 'Let\'s LIFE if ????',
        "content": 'its working  ...'
    },
    {   "id": 2,
        "title": 'world first car.....',
        "content": 'its working..'
    }
]

def home(request):
    html = ""
    for post in posts: 
        html += f'''
            <div> 
            <a href="/post/{post['id']}/">
                <h1>{post['id']} - {post['title']}</h1></a> 
                <p>{post['content']}</p> 
           </div>'''
    name = "John "    
    return render(request, 'posts/home.html', {'posts': posts, 'username':'john'})


def post(request, id,):
    valid_id = False
    for post in posts:
        if post['id'] == id: 
            post_dict = post
            valid_id = True
            break
    if valid_id:    
        return render(request, 'posts/post.html', {'post_dict':posts})
    else:
        return HttpResponseNotFound("<h1>post not found</h1>")
    

def google(request, name):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)



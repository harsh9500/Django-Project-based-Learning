from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()
    
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


# def index(request):

#     all_albums=Album.objects.all()
#     context = {
#         'all_albums' : all_albums,
#     }
#     return render(request,'music/index.html',context)

#     # html = ""
#     # for album in all_albums:
#     #     url = "/music/" + str(album.id) + "/"
#     #     html += "<a href = " + url + ">" + album.album_title + "</a><br>"
#     # return HttpResponse(html)


# def detail(request, album_id):
#     album = get_object_or_404(Album,pk=album_id)
#     return render(request,'music/detail.html',{"album":album})


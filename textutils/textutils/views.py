from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
 #   return render(request, 'index.html')
def index(request):
    dicti={'name':'I', 'place':'Mars'}
    return render(request, 'index.html', dicti)

def about(request):
    return HttpResponse('<h1>about...</h1><br> <a href="/">back</a>')  
def demo(request):
    demotext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')  

    print(removepunc)
    print(demotext)
    if(removepunc=="on"):
        punctuations = '''!()-[]{,};:'"\<>./?@#$%^&*_~'''
        analyzed= ""
        for ch in demotext:
            if ch not in punctuations:
                analyzed += ch
        param= {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html',param)
    if(fullcaps=="on"):
        analyzed = ""
        for char in demotext:
            analyzed = analyzed + char.upper()

        param = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', param)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(demotext):
            if not(demotext[index] == " " and demotext[index+1]==" "):
                analyzed = analyzed + char

        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', param)

    if (newlineremover == "on"):
        analyzed = ""
        for char in demotext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', param)
      
    else:            
        return HttpResponse("Error")      
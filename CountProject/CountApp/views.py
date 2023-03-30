from django.shortcuts import render

# Create your views here.

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(' ',''))

    blank_space_count = 0
    for a in text:
        if a == ' ':
            blank_space_count += 1
    
    word_count = blank_space_count +1

    return render(request, 'result.html', {'text': text, 'total_len': total_len, 'no_blank_len': no_blank_len, 'word_count': word_count})


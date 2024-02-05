from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


days = {
    'saturday': 'this is satureday in disctionary',
    'sunday': 'this is sunday in disctionary',
    'monday': 'this is monday in disctionary',
    'tuesday': 'this is tuesday in disctionary',
    'wednesday': 'this is wednesday in disctionary',
    'thursday': 'this is thursday in disctionary',
    'friday': None
}
def dynamic_days(reqeust, day):
    day_data = days.get(day)
    
    # YE HALAYE DIGE BARAYE PAGE NOT FOUND :
    if day_data is None:
        raise Http404()
        
        # YEK HALAT BARAYE 404 :
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
    
    
    #if day_data is not None:
        #HALATE AVAL BE SORATE DASTI : response_data = f'<h3 style="color:red"> day is : <em>{day}</em> and data is : {day_data} </h3>'
        #HALATE DOVOM RENDER TO STRING : response_data = render_to_string('Dr/index.html')
        # return HttpResponse(response_data)

    # VA AMA HALATE SEVOM VA ASLI :
    context = { 'day_data': day_data , 'day':day }
    return render ( reqeust , 'Dr/index.html' , context )        
    #return HttpResponseNotFound('day does not exists')


def days_list(request):
    days_list = list(days.keys())
    context = { 'days':days_list }
    return render ( request , 'Dr/index2.html' , context )
    
    
    
    # list_items = ""
    # for day in day_list:
    #     url_path = reverse('days-of-week', args=[day])
    #     list_items += f'<li> <a href="{url_path}"> {day} </a> </li>\n'
    # content = f'<ul>\n {list_items}\n</ul>'
    
    # return HttpResponse(content)


def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        raise Http404()
    
    elif day > len(days_names):
        return HttpResponseNotFound('day does not exists')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)

    # return HttpResponse(day)
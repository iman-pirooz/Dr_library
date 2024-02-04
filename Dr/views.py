from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



days = {
    'sunday':'this is in dictionary ***',
    'monday':'this is monday ***',
    'tuesday':'this is tuesday ***',
    'saturday':'this is saturday ***',
    'wednesday':'this is wednesday ***',
    'tursday':'this is tursday ***',
    'friday':'this is friday ***',
}

def days_list ( request ):
    content = '''
        <ul>
            
                <li> <a href = '/days/saturday' > saturday </a> </li> <br> 
                <li> <a href = '/days/sunday' > sunday </a> </li> <br>
                <li> <a href = '/days/monday' > monday </a> </li> <br>
                <li> <a href = '/days/tuesday' > tuesday </a> </li> <br>
                <li> <a href = '/days/wednesday' > wednesday </a> </li> <br>
                <li> <a href = '/days/tursday' > tursday </a> </li> <br>
                <li> <a href = '/days/friday' > friday </a> </li> <br>
            
        </ul>
    '''
    return HttpResponse(content)


def day_test_by_number ( request , day ):
    day_name = list(days.keys())
    redirect = day_name[day-1]
    return HttpResponseRedirect(redirect) 
''' ma mitonim ya toye in khat mostaghim adres bedim
    ya bayad az dastore reverse estefade konim
    sakhtare dastore reverse be shekle zire
'''
#     redirect_again = reverse('days-of-week' , args=[redirect])
#     return HttpResponseRedirect(redirect_again)

def day_test ( request , day ):
    day_data = days.get(day)
    if day_data is not None:
        response_data = f'<h1>this is {day} , {day_data}</h1>'
        return HttpResponse ( response_data )
    else:
        return HttpResponseNotFound ( 'Day Does Not Exist' )
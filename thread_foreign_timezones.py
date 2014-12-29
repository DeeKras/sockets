from atexit import register
import threading
from time import ctime
import requests


url_lookup = 'http://www.timeapi.org/{}/now'

places = {'Paris': 'cet',
            'Moscow': 'msk',
            'Kuwait':  'ast',
            'New York': 'est',
            'Copenhagen': 'cet'}

def _display_time(place):
    time_zone = places[place]
    current_time = requests.get(url_lookup.format(time_zone)).content    
    print '{:>10} | {:<15}'.format(place, current_time[11:19])

def main():
    print 'starting at:', ctime()
    print '-'*30
    for place in places:
        threading.Thread(target=_display_time, args=(place,)).start()

@register
def _atexit():
    print '-'*30
    print 'all done at:', ctime()

if __name__ == '__main__':
    main()
    
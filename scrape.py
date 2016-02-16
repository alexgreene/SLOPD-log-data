# scrape the San Luis Obispo Police Department Summary Report,
# parse the responses, then add them to the CSV.

from lxml import html
import requests
import csv

def oreo(s, start, end):
  return ((s.split(start))[1].split(end)[0]).strip()

page = requests.get('http://pdreport.slocity.org/policelog/rpcdsum.txt')
html = html.fromstring(page.content)
text = html.text_content()
cut_footer = text.split('--------------------------------------------------------------------------------')[0]
els = cut_footer.split('===============================================================================')

header = els.pop(0)
new_log_number = oreo(header, 'Police Department', '\n')

print 'DOWNLOADING SLO POLICE DATA...'

i = 0
items = []

for el in els:
    el = el.strip()

    if ( i % 2 == 0 ):
        time_data = el.split(' ')
        item = {}
        item['date'] = time_data[1]
        item['recieved'] = oreo(el, 'Received:', 'Dispatched:')
        item['dispatched'] = oreo(el, 'Dispatched:', 'Arrived:')
        item['arrived'] = oreo(el, 'Arrived:', 'Cleared:')
        item['cleared'] = oreo(el, 'Cleared:', '\n')
        items.append(item)
    else:
        items[len(items)-1]['type'] = oreo(el, 'Type:', 'Location:')
        items[len(items)-1]['observed_type'] = oreo(el, 'As Observed:', 'Addr:')
        items[len(items)-1]['location'] = oreo(el, 'Addr:', 'Clearance Code:')
        items[len(items)-1]['officer'] = oreo(el, 'Responsible Officer:', 'Units:')
        items[len(items)-1]['units'] = oreo(el, 'Units:', 'Des:')
        items[len(items)-1]['comments'] = oreo(el, 'CALL COMMENTS:', '\n')

    i += 1

update_file = open('/Users/alexg/Documents/data/slo-pd-logs/update_file.txt', 'r')
prev_log_number = update_file.read()
update_file.close()

if new_log_number != prev_log_number:
    log_file = open('/Users/alexg/Documents/data/slo-pd-logs/logfile.csv', 'a')
    wr = csv.writer(log_file)
    for item in items:
        wr.writerow([ item['date'], item['recieved'], item['dispatched'], item['arrived'], item['cleared'], 
            item['type'], item['observed_type'], item['location'], item['officer'], item['units'], item['comments']])    

    update_file = open('/Users/alexg/Documents/data/slo-pd-logs/update_file.txt', 'w')
    update_file.write(new_log_number)
    update_file.close()








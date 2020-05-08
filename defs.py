def form_date(new_date):
    new_date = new_date.split('T')
    cdate = new_date[0]
    ctime = str(new_date[1]).replace('Z', '').split(':')
    ctime[0] = int(ctime[0]) + 4
    ctime[0] = str(ctime[0])
    return 'Tarix: ' + str(cdate) + ' ' + str(':'.join(ctime))
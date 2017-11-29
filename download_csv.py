import urllib.request

def download_csv_date(url):
    response=urllib.request.urlopen(url)
    response_csv=str(response.read())
    lines=response_csv.split('\\n')
    name='csv_file'
    fw=open(name,'w')
    for line in lines:
        fw.write(line+'\n')
    fw.close()

download_csv_date('http://chart.finance.yahoo.com/table.csv?s=GOOG&a=2&b=10&c=2017&d=3&e=10&f=2017&g=d&ignore=.csv')
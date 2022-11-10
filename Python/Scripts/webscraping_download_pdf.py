from bs4 import BeautifulSoup 
import requests 
import re 

def get_html_document(url): 
    response = requests.get(url) 
    return response.text 

def save_downloaded_document(url, folder, name):
    r = requests.get(url, stream = True)
    with open((folder+name), 'wb') as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

def get_list_of_documents(downloads_list):
    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}): 
        if 'https://intranet.portodesantos.com.br/docs_codesp/doc_codesp_pdf_site.asp?id=' in link.get('href'):
            downloads_list.append(link.get('href'))


def download_documents(downloads_list):
    if len(downloads_list) != 0:
        total_documents = 0
        print(f'Initializing download of the documents: ')
        print('-'*40)
        for downloads in downloads_list:
            print(downloads)
            file_name = downloads[downloads.find('=')+1:]+'.pdf'
            save_downloaded_document(downloads,downloads_folder,file_name)
            total_documents+=1
            print('-'*len(downloads))
    else:
        print("No documents available for download.")
    return total_documents

#\Python\Scripts\reports
downloads_folder = './Scripts/reports/' 
url_to_scrape = "https://www.portodesantos.com.br/informacoes-operacionais/estatisticas/mensario-estatistico/"
html_document = get_html_document(url_to_scrape) 
soup = BeautifulSoup(html_document, 'html.parser') 
downloads_list = []

get_list_of_documents(downloads_list)

total_documents = download_documents(downloads_list)

print(f'Total of downloaded documents: {total_documents}' )


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

# Buka dokumen Google Docs yang ingin Anda gunakan
document_id = '1e8UZtMp_VTADKgd8my227kvDFf6CM3fU'

# Atur kata yang ingin Anda cari
keyword = 'YOUR_KEYWORD'

# Masukkan token akses OAuth 2.0 Anda di sini
creds = Credentials.from_authorized_user_info(info=None)

# Membangun koneksi ke layanan Google Docs
service = build('docs', 'v1', credentials=creds)

# Memanggil fungsi 'documents().get()' untuk mengambil dokumen
document = service.documents().get(documentId=document_id).execute()

# Mendapatkan seluruh elemen dalam dokumen
elements = document.get('body').get('content')

# Mencari elemen dengan kata yang diberikan
for value in elements:
  if 'textRun' in value:
    if 'content' in value['textRun']:
      if keyword in value['textRun']['content']:
        # Mengubah gaya font menjadi italic
        value['textRun']['textStyle']['italic'] = True

# Menggunakan fungsi 'documents().batchUpdate()' untuk memperbarui dokumen
result = service.documents().batchUpdate(documentId=document_id, body={
    'requests': [{
        'updateTextStyle': {
            'range': {
                'startIndex': value['startIndex'],
                'endIndex': value['startIndex'] + len(value['textRun']['content'])
            },
            'textStyle': value['textRun']['textStyle'],
            'fields': 'italic'
        }
    } for value in elements if 'textRun' in value]
}).execute()

print('Font style diubah menjadi italic.')

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os


def create_google_drive_document(data, name):
    # Путь к файлу учетных данных (предоставьте свой путь)
    credentials_path = 'credentials.json'
    token_path = 'token.json'

    creds = None

    # Загрузка учетных данных
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    # Если учетные данные не действительны или отсутствуют, запросите их у пользователя.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path,
                                                             ['https://www.googleapis.com/auth/drive.file'])
            creds = flow.run_local_server(port=0)

        # Сохраняем учетные данные для последующих запусков
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    # Строим объект для взаимодействия с Google Drive API
    service = build('drive', 'v3', credentials=creds)

    # Создаем файл
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.document'
    }

    media = {
        'mimeType': 'text/plain',
        'body': data
    }

    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    return file.get('id')
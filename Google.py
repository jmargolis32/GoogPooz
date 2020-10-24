{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import os\n",
    "from google_auth_oauthlib.flow import Flow, InstalledAppFlow\n",
    "from googleapiclient.discovery import build\n",
    "from googleapiclient.http import MediaFileUpload\n",
    "from google.auth.transport.requests import Request\n",
    " \n",
    "def Create_Service(client_secret_file, api_name, api_version, *scopes):\n",
    "    print(client_secret_file, api_name, api_version, scopes, sep='-')\n",
    "    CLIENT_SECRET_FILE = client_secret_file\n",
    "    API_SERVICE_NAME = api_name\n",
    "    API_VERSION = api_version\n",
    "    SCOPES = [scope for scope in scopes[0]]\n",
    " \n",
    "    cred = None\n",
    " \n",
    "    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'\n",
    "    # print(pickle_file)\n",
    " \n",
    "    if os.path.exists(pickle_file):\n",
    "        with open(pickle_file, 'rb') as token:\n",
    "            cred = pickle.load(token)\n",
    " \n",
    "    if not cred or not cred.valid:\n",
    "        if cred and cred.expired and cred.refresh_token:\n",
    "            cred.refresh(Request())\n",
    "        else:\n",
    "            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)\n",
    "            cred = flow.run_local_server()\n",
    " \n",
    "        with open(pickle_file, 'wb') as token:\n",
    "            pickle.dump(cred, token)\n",
    " \n",
    "    try:\n",
    "        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)\n",
    "        print(API_SERVICE_NAME, 'service created successfully')\n",
    "        return service\n",
    "    except Exception as e:\n",
    "        print(e)\n",
    "    return None\n",
    " \n",
    "def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):\n",
    "    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'\n",
    "    return dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

When deploying to Azure, try not to upload the actual model to Web server,
instead the startup script will download the actual model from Google Drive.
Also, if running locally, don't forget to set FLASK_APP=hello:myapp. (IF NEEDED)

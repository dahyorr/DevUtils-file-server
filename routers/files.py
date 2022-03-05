import os
from fastapi import FastAPI, FastAPI, UploadFile, File, Depends, APIRouter
from fastapi.responses import JSONResponse
from dependencies.security import verify_api_key
from fastapi.security.api_key import APIKey
from config import UPLOAD_PATH, ORIGINS


router = APIRouter(
  tags=["Files"],
  dependencies=[Depends(verify_api_key)],
)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), api_key: APIKey = Depends(verify_api_key)): # TODO: check if file exists first
    with open(f'{UPLOAD_PATH}/{file.filename}', 'wb') as uploadedFile:
        content = await file.read()
        uploadedFile.write(content)
        uploadedFile.close()
    return JSONResponse(content={
        "filename": file.filename,
        "message":"File Uploaded Successfully"
        }, status_code=200)

@router.delete("/delete/file/{file_name}")
def delete_file(file_name: str):
    print(file_name)
    try:
        print(f'{UPLOAD_PATH}/{file_name}')
        os.remove(f'{UPLOAD_PATH}/{file_name}')
        return JSONResponse(content={
            "message": "File Deleted Successfully"
            }, status_code=200)   
    except FileNotFoundError:
        return JSONResponse(content={
            "message": "File not found"
        }, status_code=404)
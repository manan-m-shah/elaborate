from fastapi import APIRouter, Depends
from app.services.github_service import fetch_repository_files, fetch_file_content

router = APIRouter()

@router.get("/get_repository_files")
async def get_repository_files(repo_owner: str, repo_name: str, access_token: str):
    files = fetch_repository_files(repo_owner, repo_name, access_token)
    return {"files": files}

@router.get("/get_file_content")
async def get_file_content(repo_owner: str, repo_name: str, file_path: str, access_token: str):
    content = fetch_file_content(repo_owner, repo_name, file_path, access_token)
    return {"content": content}

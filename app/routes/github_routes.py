import os
import time
from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.github_service import fetch_repo, fetch_repository_files, fetch_file_content
from app.secrets import GITHUB_ACCESS_TOKEN

router = APIRouter()

@router.get("/repo")
async def get_repo(repo_owner: str, repo_name: str):
    content = fetch_repo(repo_owner, repo_name)
    return FileResponse(content, filename=f"{repo_owner}_{repo_name}.txt")

@router.get("/get_repository_files")
async def get_repository_files(repo_owner: str, repo_name: str):
    files = fetch_repository_files(repo_owner, repo_name)
    return {"files": files}

@router.get("/get_file_content")
async def get_file_content(repo_owner: str, repo_name: str, file_path: str):
    content = fetch_file_content(repo_owner, repo_name, file_path)
    return {"content": content}

@router.get("/test")
async def test():
    return GITHUB_ACCESS_TOKEN

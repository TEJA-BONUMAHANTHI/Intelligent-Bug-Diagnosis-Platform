from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional

from app.services.bug_processor import process_bug


router = APIRouter()


@router.post("/submit")
async def submit_bug(
    title: str = Form(...),
    description: str = Form(...),
    stack_trace: Optional[str] = Form(None),
    error_log: Optional[str] = Form(None),
    severity: str = Form("Medium"),
    file: Optional[UploadFile] = File(None)
):
    if not title.strip():
        raise HTTPException(
            status_code=400,
            detail="Bug title cannot be empty"
        )

    if not description.strip():
        raise HTTPException(
            status_code=400,
            detail="Bug description cannot be empty"
        )

    file_name = None
    file_content = None

    if file:
        allowed_extensions = [".txt", ".log", ".md"]

        if not any(
            file.filename.lower().endswith(ext)
            for ext in allowed_extensions
        ):
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type. Use TXT, LOG or MD files."
            )

        file_content = await file.read()
        file_name = file.filename

        if len(file_content) == 0:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty"
            )

    processed_bug = process_bug(
        title=title,
        description=description,
        stack_trace=stack_trace,
        error_log=error_log
    )

    if file_content:
        try:
            uploaded_text = file_content.decode("utf-8")
            processed_bug["uploaded_file_content"] = uploaded_text
        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file must contain UTF-8 text."
            )

    processed_bug["severity"] = severity
    processed_bug["file_name"] = file_name
    processed_bug["status"] = "Submitted"

    return {
        "message": "Bug submitted successfully",
        "bug": processed_bug
    }
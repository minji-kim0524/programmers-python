from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    content = await file.read()

    if filename.endswith('.csv'):
        return {"message": f"CSV file '{filename}' uploaded successfully.", "content_length": len(content)}
    elif filename.endswith('.xlsx'):
        return {"message": f"Excel file '{filename}' uploaded successfully.", "content_length": len(content)}
    else:
        return {"message": f"Unsupported file type for '{filename}'. Please upload a CSV or Excel file."}
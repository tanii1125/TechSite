def upload_pdf(db,fs,file):
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Save PDF in GridFS
    file_id = fs.put(file, filename=file.filename)

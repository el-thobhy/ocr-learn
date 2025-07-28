def allowed_file(filename: str, allowed_exts: list[str]) -> bool:
    return any(filename.lower().endswith(ext) for ext in allowed_exts)
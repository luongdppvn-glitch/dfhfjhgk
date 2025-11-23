with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    if search_text in content:
                        content = content.replace(search_text, replace_text)
                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        msg = f"✅ Đã sửa file: {full_path}"

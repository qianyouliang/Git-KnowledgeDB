from core.modelback import ModelBack
from core.file2markdown import File2Markdown
from core.folder2vdb import FolderToFaissDB
from datetime import datetime
import os

def main():
    model_back = ModelBack()
    file_to_markdown = File2Markdown("./input", "./output")
    folder_to_vdb = FolderToFaissDB("./output")
    role_prompt = '我是一名博客作者，我会根据得到的代码或内容，撰写这个代码或文档的实现的详细功能，描述每个函数代码的思路，并将其撰写markdown格式的代码文档和技术博客；我会遵守文章撰写的规范和逻辑，保持文章内容的准确性和清晰度。用中文撰写'

    files = file_to_markdown.list_github_directory()
    for file_info in files:
        if file_info['type'] == 'file':
            content = file_to_markdown.extract_file_content(os.path.join("./input", file_info['name']))
            if content:
                blog_content = model_back.generate(role_prompt, "当前代码如下:开始撰写"+content) + '\n\n' +"源内容如下："+'```' + '\n' + content + '\n' + '```'
                if blog_content:
                    db_name = input(f"Enter the database name for {file_info['name']} (without spaces): ")
                    file_to_markdown.write_to_markdown(f"{datetime.now().strftime('%Y-%m-%d')}-{file_info['name']}.md", blog_content)
                    blog_to_faiss_db.add_document(blog_content)
    
    # 所有博客内容生成完毕后，创建向量数据库
    if blog_contents:
        db_name = input("Enter the database name for the collected contents (without spaces): ")
        folder_to_faiss_db.process_all_documents(db_name)

if __name__ == "__main__":
    main()

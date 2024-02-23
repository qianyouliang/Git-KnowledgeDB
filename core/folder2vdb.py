import os
from datetime import datetime
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.pdf.PyPDFLoader # 加载pdf
from langchain_community.document_loaders import NotebookLoader # 加载ipynb
from langchain_openai import OpenAIEmbeddings

class FolderToFaissDB:
    def __init__(self, output_folder, db_save_path='./KnowledgeDB'):
        self.output_folder = output_folder
        self.db_save_path = db_save_path
        self.embeddings = OpenAIEmbeddings()
        self.documents = []  # 存储所有生成的博客内容

    def add_document(self, content):
        # 添加生成的博客内容到列表中
        self.documents.append(content)

    def process_all_documents(self,db_name):
        # 检查是否有文档要处理
        if self.documents:
            # 创建向量数据库
            db = self.create_faiss_db(self.documents)
            self.save_faiss_db(db, db_name)

    def create_faiss_db(self, documents):
        # 使用所有文档内容创建向量数据库
        return FAISS.from_documents(documents, self.embeddings)

    def save_faiss_db(self, db, db_name):
        # 创建数据库保存路径
        db_save_folder = os.path.join(self.db_save_path, db_name)
        if not os.path.exists(db_save_folder):
            os.makedirs(db_save_folder)
        db_save_file = os.path.join(db_save_folder, "faiss_index")
        # 保存数据库
        db.save_local(db_save_file)
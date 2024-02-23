import os

class File2Markdown:
    def __init__(self, input_folder, output_folder='./KnowledgeDB'):
        self.input_folder = input_folder
        self.output_folder = output_folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def extract_file_content(self, file_path):
        """
        提取文件内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None
        
    def list_github_directory(self):
        def list_directory(directory):
            files = []
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    files.append({
                        'type': 'directory',
                        'name': item,
                        'content': list_directory(item_path)
                    })
                else:
                    files.append({'type': 'file', 'name': item})
            return files
        return list_directory(self.input_folder)


    def write_to_markdown(self, file_name, content):
        output_file = os.path.join(self.output_folder, file_name)
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as exc:
            print(f"Error writing to file {output_file}: {exc}")
        

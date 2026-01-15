class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Generate():
    def generate_pdf(self):
        print("PDF generated")

class Save():
    def save_to_file(self, filename):
        print(f"Saved {filename}")

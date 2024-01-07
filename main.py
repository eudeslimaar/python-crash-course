import os

# Base directory where your files are located
base_directory = 'solutions'


def create_links(directory, owner, repository):
    links = []
    for root_folder, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root_folder, file)
            url_path = f"https://github.com/{owner}/{repository}/tree/main/{file_path.replace(os.sep,'/')}"
            file_link = f"[{file}]({url_path})"
            links.append(file_link)
    return links


generated_links = create_links(base_directory, "eudeslimaar", "python-crash-course")

for link in generated_links:
    print(link)

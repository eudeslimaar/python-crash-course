import os
import datetime


def get_creation_date(file_path):
    if os.path.exists(file_path):
        file_info = os.stat(file_path)
        creation_date_timestamp = file_info.st_ctime
        creation_date = datetime.datetime.fromtimestamp(creation_date_timestamp)
        return creation_date
    else:
        return None


def create_links(directory, owner, repository):

    main_readme = "# Object-oriented Python\n\n"

    for root_folder, subfolders, _ in os.walk(directory):
        for subfolder in subfolders:
            subdirectory_path = os.path.join(root_folder, subfolder)
            readme_path = os.path.join(subdirectory_path, 'README.md')

            if not subfolder.lower() == directory:
                links = []

                files_with_dates = [
                    (file, get_creation_date(os.path.join(subdirectory_path, file)))
                    for file in os.listdir(subdirectory_path)
                    if file.lower() != 'readme.md'
                ]

                files_with_dates = [(file, date) for file, date in files_with_dates if date is not None]

                files_with_dates.sort(key=lambda x: x[1])

                count = 1
                for file, _ in files_with_dates:
                    file_path = os.path.join(subdirectory_path, file)
                    url_path = f"https://github.com/{owner}/{repository}/tree/main/{file_path.replace(os.sep, '/')}"
                    file_link = f"{count}. [{file.replace(".py", "")}]({url_path})"
                    links.append(file_link)

                    count += 1

                with open(readme_path, 'w', encoding='utf-8') as readme_file:
                    readme_file.write('\n'.join(links))

                print(f"README.md file created in {subdirectory_path}")

                main_readme += (f"- [{os.path.relpath(subdirectory_path, directory).title().replace("_", " ")}](https://github.com/{owner}/{repository}/tree/main/{directory}/"
                                f"{os.path.relpath(subdirectory_path, directory).replace(os.sep, '/')})\n")

    main_readme_path = os.path.join('./', 'README.md')
    with open(main_readme_path, 'w', encoding='utf-8') as main_readme_file:
        main_readme_file.write(main_readme)

    print(f"Main README.md file updated!")


create_links('solutions', 'eudeslimaar', 'python-crash-course')



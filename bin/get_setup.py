from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from pathlib import Path



#change this to get setup docs
log.info(f"Getting lesson with parameters:\n org-name: {org_name} \n gh-name: {lesson_name} \n branch: {gh_branch} \n type: {lesson_type.value}")
os.system(f"git submodule add --force -b {gh_branch} https://github.com/Southampton-RSG-Training/{lesson_name}.git submodules/{lesson_name}")
os.system("git submodule update --remote --merge")


# get list of setup.md chunks from _config.yml and apply order to them
# Open the website config, which contains a list of the lessons we want in the
# workshop, then create the directory "submodules" which will contain the files
# for each lesson
with open('_config.yml') as config:
    website_config = load(config, Loader=Loader)
log.info(f"Getting submodules specified in {website_config['lessons']}")
Path("submodules").mkdir(parents=True, exist_ok=True)


# open setup.md
# loop to make the setup.md file
        # append each of the .md setup chunks to setup.md

#this should be moved to a chunk
setup_md_string = """
## Setup

### Text Editor

A text editor is the piece of software you use to view and write code. If you
have a preferred text editor, please use it. Suggestions for text editors are,
Notepad++ (Windows), TextEdit (macOS), Gedit (GNU/Linux), GNU Nano, Vim.
Alternatively, there are IDE's (integrated developer environments) that have
more features specifically for coding such as VS Code; there are also IDEs
specific to languages will be listed in the appropriate section(s) below.
"""

for lesson in date_sorted_lessons:

    filename = f"_includes/rsg/{lesson['gh-name']}-lesson/setup.md"
    content, head = get_file_and_head(filename)
    content = content.splitlines()

    # Next, change the depth of the headings
    for i, line in enumerate(content):
        if line.startswith("#"):
            line = line.rstrip("#")
            nhashes = line.count("#") + 2
            if nhashes > 5:
                nhashes = 5
            line = "#" * nhashes + line.lstrip("#")
            content[i] = line

    setup_md_string += "\n### {}\n\n{}\n".format(lesson["title"], "\n".join(content))

    # write out the new setup.md file to the root directory

with open("setup.md", "w") as fp:
    fp.write(setup_md_string)

done

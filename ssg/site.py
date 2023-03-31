import typer
from pathlib import Path
from ssg.site import Site

class Site:
    def __init__(self, source, dest):
        self.source = source.Path()
        self.dest = dest.Path()
    
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

def main():
    source = "content"
    dest = "dist"

    config = {}

    config["source"] = source
    config["dest"] = dest

    Site = Site(**config)
    Site.build()

typer.run(main)


       






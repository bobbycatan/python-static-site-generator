import typer

from ssg.site import Site

def main():
    source = "content"
    dest = "dist"

    config = {}

    config["source"] = source
    config["dest"] = dest

    Site = Site(**config)
    Site.build()

typer.run(main)
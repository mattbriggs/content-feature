'''
Workflow for module for graphing TOCs.

2022.11.17 Matt Briggs
'''

import yaml
import mdbutilities.mdbutilities as MU

import tocharvestor as TH
import tocscanner as TS
import tocformats as TF

def main():

    with open (r"C:\git\feature\content-feature\ex-003\jobtoc.yml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    output = ""
    for i in config["folders"]:
        tocs = TH.get_tocs_from_repo(i["folder"])
        size = len(tocs)
        for count, t, in enumerate(tocs):
            print("{} of {} getting {}".format(size-count, size, t))
            graphed = TS.input_tocfile(t)
            output += TF.create_cypher_text(graphed)

    MU.write_text(output, config["output"])


if __name__ == "__main__":
    main()
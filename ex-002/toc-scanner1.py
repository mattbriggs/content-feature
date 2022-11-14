'''This scripts work and unpacks a table of contents as a flat list.
It specifies the filename and document type (ms.topic)

2022.11.12 Matt Briggs
'''


from re import X
import sys
import yaml
import mdbutilities.mdbutilities as MU
import markdownvalidator.mdhandler as MDH

# C:\git\ms\azure-docs-pr\articles\active-directory\app-provisioning\toc.yml

def main():
    ''' '''
    try: 
        tocfile = sys.argv[1]
    except IndexError as e:
        tocfile = r"C:\git\ms\azure-docs-pr\articles\active-directory\app-provisioning\toc.yml"
        # print("Error: {}\nNeed a toc file.".format(e))
        # exit()

    with open (tocfile, "r") as stream:
        tocdict = yaml.load(stream, Loader=yaml.CLoader)

    print(tocdict)

    spot = tocfile.lower().find("toc.yml")
    stem = tocfile[0:spot]


# dict is a node.
# need to store a node
# string are the values in the node.


    def process_toc(intoc):
        if type(intoc) == str:
            print(intoc)
            if intoc.find(".md") > 0:
                try:
                    handler = MDH.MDHandler()
                    md_page = handler.get_page(stem + str(intoc))
                    print(md_page.metadata["ms.topic"])
                except:
                    print(stem + str(intoc))
        elif type(intoc) == list:
            for i in intoc:
                process_toc(i)
        elif type(intoc) == dict:
            for i in intoc.keys():
                process_toc(intoc[i])

    process_toc(tocdict)

if __name__ == "__main__":
    main()
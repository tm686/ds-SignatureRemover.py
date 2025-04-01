import sys
import xml.etree.ElementTree as ET
import os

def remove_ds_signatures(xml_input_path, xml_output_path):
    ET.register_namespace('ds', "http://www.w3.org/2000/09/xmldsig#")
    tree = ET.parse(xml_input_path)
    root = tree.getroot()

    # Remove <ds:Signature> blocks from the root and children
    for elem in root.iter():
        for child in list(elem):
            if child.tag.endswith("Signature") and "http://www.w3.org/2000/09/xmldsig#" in child.tag:
                elem.remove(child)

    tree.write(xml_output_path, encoding="utf-8", xml_declaration=True)
    print(f"[+] Cleaned XML saved to: {xml_output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <input_file.xml>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"[-] File not found: {input_file}")
        sys.exit(1)

    output_file = f"cleaned_{os.path.basename(input_file)}"
    remove_ds_signatures(input_file, output_file)

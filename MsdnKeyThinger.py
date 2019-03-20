import argparse

from MsdnXmlProcessor import MsdnXmlProcessor


def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('file', help='path to input .xml file', type=str)
    return ap.parse_args()


args = get_args()
processor = MsdnXmlProcessor(None)
processor.read_xml_file(args.file)

processor.print_subscriptions()
processor.print_product_keys()

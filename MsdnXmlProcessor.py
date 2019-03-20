import xml.etree.ElementTree as eltree


class MsdnXmlProcessor:
    def __init__(self, root):
        self._root = root

    def read_xml_file(self, xml_file):
        self._root = eltree.parse(xml_file).getroot()

    def print_product_keys(self):
        print("\t*** Keys ***")

        for product_key in self._root.findall('./YourKey/Product_Key'):
            print('{}:'.format(product_key.attrib['Name']))

            for key in product_key.findall('./Key'):
                if 'ClaimedDate' not in key.attrib:
                    key.attrib['ClaimedDate'] = 'N/A'

                if 'Notes' not in key.attrib:
                    key.attrib['Notes'] = ''

                print('\t{}\tType: {}\tID: {}\tClaimed: {}\tNotes: {}'.format(key.text, key.attrib['Type'], key.attrib['ID'], key.attrib['ClaimedDate'], key.attrib['Notes']))

    def print_subscriptions(self):
        print("\t*** Subscriptions ***")

        for subscription in self._root.findall('./YourSubscription/Subscription'):
            print('{}:'.format(subscription.attrib['Name']))

            for guid in subscription.findall('./SubscriptionGuid'):
                print('\t{}'.format(guid.text))

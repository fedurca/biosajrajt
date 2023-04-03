import json

class Data:
    def __init__(self):
        with open('data.json') as f:
            self.data = json.load(f)
        self.objects = []
        for item in self.data:
            obj = {}
            for key in item.keys():
                if key.startswith('ref_'):
                    ref_key = key.replace('ref_', '')
                    ref_item = next((x for x in self.data if x['kod_cs'] == item[key]), None)
                    if ref_item:
                        obj[ref_key] = ref_item[ref_key]
                else:
                    obj[key] = item[key]
            self.objects.append(obj)

    def get_data(self):
        return self.data

    def get_objects(self):
        return self.objects

    def present_data(self):
        for obj in self.objects:
            print(obj)

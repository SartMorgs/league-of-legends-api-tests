import json


class Writer:
    def __init__(self, path):
        self.path = path

    def __dict_to_json(self, json_as_dict):
        return json.dumps(json_as_dict, indent=4)

    def _write_json(self, json_content, json_filename):
        filename = f'{self.path}/{json_filename}.json'

        with open(filename, 'w') as json_file:
            json_file.write(json_content)

    def _write_dict_as_json(self, json_as_dict, json_filename):
        json_object = self.__dict_to_json(json_as_dict)
        self._write_json(json_object, json_filename)

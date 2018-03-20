import csv
import json
import xml

class Converter():

    @staticmethod
    def toJSON(source):
        is_json = True

        try:
            json_object = json.loads(source)
        except ValueError, e:
            is_json = False

        print("is valid JSON", is_json)
        if(is_json):
            return source

        #convert to json

    @staticmethod
    def toCSV(source):
        print("to csv", source)

    @staticmethod
    def toXML(source):
        print("to csv", source)

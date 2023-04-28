from jsonschema import Draft7Validator
import pandas as pd

# JSON schema from part 1 and part 2 of the message
schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "properties": {
        "cislo": {
            "$ref": "#/definitions/CisloUnion"
        },
        "kod_parametru": {
            "$ref": "#/definitions/KodParametr"
        },
        "info": {
            "$ref": "#/definitions/Info"
        },
        "error": {
            "$ref": "#/definitions/Error"
        },
        "CSVarList": {
            "$ref": "#/definitions/CSVarList"
        }
    },
    "required": [
        "cislo",
        "kod_parametru"
    ],
    "title": "CSVarListResponse",
    "definitions": {
        "CT": {
            "type": "string"
        },
        "PlatnostDo": {
            "type": "string",
            "format": "date-time"
        },
        "PlatnostOd": {
            "type": "string",
            "format": "date-time"
        },
        "CSVarList": {
            "type": "object",
            "properties": {
                "msgs": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Msg"
                    }
                },
                "sluzby": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "integer"
                    }
                },
                "telefon": {
                    "type": "string"
                },
                "prezentace": {
                    "$ref": "#/definitions/Prezentace"
                },
                "produkty": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "integer"
                    }
                },
                "provozni_doba": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/ProvozniDoba"
                    }
                },
                "kod_cs": {
                    "type": "string",
                    "format": "integer"
                }
            },
            "required": [
                "kod_cs",
                "msgs",
                "produkty",
                "provozni_doba",
                "sluzby",
                "telefon"
            ],
            "title": "CSVarList"
        },
        "Msg": {
            "type": "object",
            "properties": {
                "kratky_text": {
                    "$ref": "#/definitions/KratkyText"
                },
                "poradi": {
                    "type": "integer"
                },
                "dlouhy_text": {
                    "$ref": "#/definitions/DlouhyText"
                },
                "uziv_text": {
                    "type": "string"
                },
                "typ_zpravy": {
                    "type": "integer"
                }
            },
            "required": [
                "dlouhy_text",
                "kratky_text",
                "poradi",
                "typ_zpravy",
                "uziv_text"
            ],
            "title": "Msg"
        },
        "Prezentace": {
            "type": "object",
        }
    }
}

with open('cepro_data.json', 'r') as f:
    data = json.load(f)

#Validate against JSON schema
validator = Draft7Validator(schema)
errors = list(validator.iter_errors(data))
if errors:
    print(errors)
import json


class GraphQLQueryBuilder:
    def __init__(self):
        self.fields = None
        self.return_vals = None
        self.closing_brackets = ''
        self.quoted_args = ['group_id', 'item_name', 'column_value']
        self.specially_encoded_fields = ['column_values']
        super(GraphQLQueryBuilder, self).__init__()

    @staticmethod
    def monday_json_stringify(value):
        # This is necessary because Monday's API says that it requires a JSON encoded string for JSON values
        # What it ACTUALLY requires (anything else returns an error) is a JSON encoded, JSON encoded string.
        # I have tried and had fail requests that were only "dumped" once.
        # According to their API, a proper value for label should look like this:
        # "{\"label\":\"Done\"}"

        return json.dumps(json.dumps(value))

    def encode_values(self, key, value):
        if key in self.quoted_args:
            value = '"{value}"'.format(value=value)
        elif key in self.specially_encoded_fields:
            return self.monday_json_stringify(value)
        return value

    def format_return_value(self, return_value):
        values = return_value.split('.')
        return "{column} {{ {values} }}".format(column=values.pop(0), values=",".join(values)) if len(values) > 1 \
            else values[0]

    def query_fields(self, query_type, **kwargs):
        # Very, very brutish handling of nested query fields. Needs refinement.
        if self.fields:
            new_fields = ", ".join(["{key}: {value}".format(key=key, value=self.encode_values(key, value))
                                    for key, value in kwargs.items()])
            self.fields = '{existing_fields} {{ {query_type}({new_fields}) '.format(existing_fields=self.fields,
                                                                                    query_type=query_type,
                                                                                    new_fields=new_fields)
            self.closing_brackets += '}'
        else:
            query_field_string = ", ".join(
                ["{key}: {value}".format(key=key, value=self.encode_values(key, value)) for key, value in
                 kwargs.items()])
            self.fields = '{query_type}({fields})'.format(query_type=query_type, fields=query_field_string)
        return self

    def return_values(self, return_values: list):
        self.return_vals = ", ".join([self.format_return_value(value) for value in return_values])
        return self

    def make_query(self, operation: str) -> str:
        return "{operation}{{ {query_fields} {{ {return_vals} }} }} {closing_brackets}".format(operation=operation,
                                                                                               query_fields=self.fields,
                                                                                               return_vals=self.return_vals,
                                                                                               closing_brackets=self.closing_brackets)

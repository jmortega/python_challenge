import boto3

from aws_credential_helper import aws_credential_helper


class eventbridge_rules:

    def __init__(self):
        '''
        Initialize a reusable, authenticated boto3 client for Eventbridge in _events_client
        Set the lab bucket name in _bucket 
        '''
        self._events_client = aws_credential_helper.create_new_session().client('events')

    def get_rules(self):
        '''
        Return a list of the rules in the default event bus.
        '''
        return self._events_client.list_rules()['Rules']

    def update_rule_schedule(self, rule, schedule):
        '''
        Update the rule schedule for the provided rule. The values
        for the rule's Name, State, Description, and EventBusName must remain 
        the same and must not be replaced with null values.
        The function should preserve the number of rules, i.e. there should be
        only one rule before and after running this function.
        Arguments
        rule: The rule dictionary to update the schedule of.
        schedule: The new schedule string to replace the existing rule's schedule.
        '''

        # ====================================
        # Do not change the code before this

        # CODE3: Write code that completes the function as described in the docstring
        self._events_client.put_rule( Name=rule['Name'],ScheduleExpression=schedule,
        State=rule['State'],Description=rule['Description'],EventBusName=rule['EventBusName'])


if __name__ == '__main__':
    rules = eventbridge_rules()
    # This prints all the existing rules
    print(rules.get_rules())
    rules.get_rules()[0]


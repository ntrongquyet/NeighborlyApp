import logging

import azure.functions as func


def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Udacity Trigger"

    messsage = {
        "personalizations": [{
            "to": [{
                    "email": "ntrongquyet37@gmail.com"
                }]}],
        "subject": "[Udacity Trigger Subject] email",
        "content": [{
            "type": "text/plain",
            "value": value }]}
    
    sendGridMessage.set(json.dumps(message))
    return func.HttpResponse("Message successfully sent.")

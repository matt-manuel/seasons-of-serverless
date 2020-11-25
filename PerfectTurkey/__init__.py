import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    weight = req.params.get('weight')
    if not weight:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            weight = req_body.get('weight')

    if weight:
        weight = float(weight)
        salt = 0.05 * weight
        water = 0.66 * weight
        sugar = 0.13 * weight
        shallots = 0.2 * weight
        garlic = 0.4 * weight
        peppercorns = 0.13 * weight
        juniper = 0.13 * weight
        rosemary = 0.13 * weight
        thyme = 0.06 * weight
        brinetime = 2.4 * weight
        roasttime = 15 * weight
        
        return func.HttpResponse(f"Salt (cups) = {salt}\nWater (gallons) = {water}\nBrown sugar (cups) = {sugar}\nShallots = {shallots}\nCloves of garlic = {garlic}\nWhole peppercorns (tablespoons) = {peppercorns}\nDried juniper berries (tablespoons) = {juniper}\nFresh rosemary (tablespoons) = {rosemary}\nThyme (tablespoons) = {thyme}\n\nBrine time (hours) = {brinetime}\n\nRoast time (minutes) = {roasttime}\n")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a weight in the query string or in the request body for a personalized response.",
             status_code=200
        )

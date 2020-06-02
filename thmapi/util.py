import requests

root_url = 'https://tryhackme.com'


def http_get(session, path, res_format="json", has_success=False):
    """
    HTTP GET call wrapper

    :type session: requests.Session
    :param session: HTTP Session
    :type path: string
    :param path: HTTP Route
    :type res_format: string
    :param res_format: Response format
    :type has_success: bool
    :param has_success: Does the request have a "success" field
    :return: Return object
    """

    try:
        r = session.get(f'{root_url}{path}')

        if r.status_code == 200:
            if res_format == 'json':
                if has_success:
                    res = r.json()

                    if res['success']:
                        return res
                    else:
                        if 'message' in res:
                            raise Exception(f'API Error: {res["message"]}')
                        else:
                            raise Exception(f'API Error (no reason given)\nResponse: {res}')
                else:
                    return r.json()
            else:
                return r.content.decode('utf-8')
        else:
            raise Exception('HTTP Response was not 200')
    except Exception as err:
        raise err

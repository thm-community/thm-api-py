import requests
import re

__root_url = 'https://tryhackme.com'
__csrf_script_regex = re.compile("const csrfToken='(.{36})';")
__csrf_input_regex = re.compile('<input type="hidden" name="_csrf" value="(.{36})">')


def http_get(session, path, res_format="json", has_success=False, headers={}):
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
    :type headers: dict
    :param headers: Additional headers
    :return: Return object
    """

    try:
        r = session.get(f'{__root_url}{path}', headers=headers)

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


def fetch_pattern(session, path, pattern):
    """
    Fetches a pattern from a raw HTTP response

    :param session: Session
    :param path: HTTP Path
    :param pattern: Compiled regular expression ID (csrf-input/csrf-script)
    :return: String matching group 1
    """

    r = http_get(session, path, res_format='')

    if pattern == 'csrf-input':
        return __csrf_input_regex.search(r).group(1)
    elif pattern == 'csrf-script':
        return __csrf_script_regex.search(r).group(1)
    else:
        return ""


def http_post(session, path, data, res_format="json", has_success=False, headers={}):
    """
    HTTP POST call wrapper

    :type session: requests.Session
    :param session: HTTP Session
    :type path: string
    :param path: HTTP Route
    :type data: dict
    :param data: HTTP Data (JSON)
    :type res_format: string
    :param res_format: Response format
    :type has_success: bool
    :param has_success: Does the request have a "success" field
    :type headers: dict
    :param headers: Additional headers
    :return: Return object
    """

    try:
        r = session.post(f'{__root_url}{path}', json=data, headers=headers)

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
            raise Exception(f'HTTP Response was not 200 (got {r.status_code})')
    except Exception as err:
        raise err

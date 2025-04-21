"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import json
from connectors.core.connector import ConnectorError, get_logger
from .zscalar_api_auth import *
from constants import *

logger = get_logger('zscaler-client-connector')


def make_rest_call(config, endpoint, method="GET", data=None, params=None, connector_info=None):
    try:
        za = ZscalerAuth(config)
        token = za.ensure_token()
        url = za.host + endpoint
        logger.debug(f"Endpoint: {url}")
        headers = {
            'auth-token': token,
            'Content-Type': 'application/json'
        }
        logger.debug(f"Headers: {headers}")
        response = requests.request(method, url, data=data, params=params, headers=headers, verify=za.verify_ssl)
        logger.debug(f"Response [{response.status_code}]: {response.content}")

        if response.ok or response.status_code == 204:
            logger.info(f"Successfully received response from {url}")
            if 'json' in str(response.headers.get('Content-Type', '')):
                return response.json()
            return response.text
        else:
            logger.error(f"Error [{response.status_code}]: {response.text}")
            raise ConnectorError(f"{response.status_code}: {response.text}")

    except requests.exceptions.SSLError:
        raise ConnectorError('SSL certificate validation failed')
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError('Connection to the server timed out')
    except requests.exceptions.ReadTimeout:
        raise ConnectorError('The server did not respond in the allotted time')
    except requests.exceptions.ConnectionError:
        raise ConnectorError('Connection error or invalid credentials')
    except Exception as err:
        logger.exception("Unexpected error occurred")
        raise ConnectorError(str(err))


def remove_empty_values(obj):
    if isinstance(obj, dict):
        return {
            k: remove_empty_values(v)
            for k, v in obj.items()
            if v not in ("", None, []) and remove_empty_values(v) != {}
        }
    elif isinstance(obj, list):
        return [remove_empty_values(v) for v in obj if v not in ("", None, [])]
    else:
        return obj


def get_enrolled_device_list(config, params, connector_info):
    endpoint = '/papi/public/v1/getDevices'
    params = remove_empty_values(params)
    return make_rest_call(config, endpoint=endpoint, params=params, connector_info=connector_info)


def get_enrolled_device_details(config, params, connector_info):
    endpoint = '/papi/public/v1/getDeviceDetails'
    params = remove_empty_values(params)
    return make_rest_call(config, endpoint=endpoint, params=params, connector_info=connector_info)


def get_device_otp(config, params, connector_info):
    endpoint = '/papi/public/v1/getOtp'
    params = remove_empty_values(params)
    return make_rest_call(config, endpoint=endpoint, params=params, connector_info=connector_info)


def get_device_app_profile_password(config, params, connector_info):
    endpoint = '/papi/public/v1/getPasswords'
    params = remove_empty_values(params)
    return make_rest_call(config, endpoint=endpoint, params=params, connector_info=connector_info)


def download_device_details(config, params, connector_info):
    endpoint = '/papi/public/v1/downloadDevices'
    os_types = params.get('osTypes')
    if os_types:
        os_type_string = ",".join(str(OS_TYPES.get(os_type)) for os_type in os_types if OS_TYPES.get(os_type))
        params.update({'osTypes': os_type_string})
    registrationTypes = params.get('registrationTypes')
    if registrationTypes:
        res_type_string = ",".join(
            str(REGISTRATION_TYPES.get(res_type)) for res_type in registrationTypes if REGISTRATION_TYPES.get(res_type))
        params.update({'registrationTypes': res_type_string})
    params = remove_empty_values(params)
    return make_rest_call(config, endpoint=endpoint, params=params, connector_info=connector_info)


def download_service_status_of_devices(config, params, connector_info):
    endpoint = '/papi/public/v1/downloadServiceStatus'
    os_types = params.get('osTypes')
    if os_types:
        os_type_string = ",".join(str(OS_TYPES.get(os_type)) for os_type in os_types if OS_TYPES.get(os_type))
        params.update({'osTypes': os_type_string})
    registrationTypes = params.get('registrationTypes')
    if registrationTypes:
        res_type_string = ",".join(
            str(REGISTRATION_TYPES.get(res_type)) for res_type in registrationTypes if REGISTRATION_TYPES.get(res_type))
        params.update({'registrationTypes': res_type_string})
    params = remove_empty_values(params)
    return make_rest_call(config, endpoint=endpoint, params=params, connector_info=connector_info)


def execute_an_api_call(config, params, connector_info):
    try:
        endpoint = params.get("endpoint")
        http_method = params.get("method")
        query_params = params.get("query_params") if params.get("query_params") else {}
        payload = params.get("payload") if params.get("payload") else {}
        logger.debug("Payload: {0}".format(payload))
        response = make_rest_call(config, endpoint=endpoint, method=http_method, params=query_params,
                                  data=json.dumps(payload),
                                  connector_info=connector_info)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def _check_health(config, connector_info):
    try:
        result = get_enrolled_device_list(config, params={}, connector_info=connector_info)
        if result:
            return True
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise ConnectorError(str(e))


operations = {
    'get_enrolled_device_list': get_enrolled_device_list,
    'get_enrolled_device_details': get_enrolled_device_details,
    'get_device_otp': get_device_otp,
    'get_device_app_profile_password': get_device_app_profile_password,
    'download_device_details': download_device_details,
    'download_service_status_of_devices': download_service_status_of_devices,
    'execute_an_api_call': execute_an_api_call
}

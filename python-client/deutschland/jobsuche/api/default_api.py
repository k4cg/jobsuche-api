"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8. **Achtung**: der OAuth header muss 'OAuthAccessToken' heißen.<br><br> Die API verfügt außerdem nicht über ein gültiges TLS Zertifikat. Deswegen sollte die TLS-Validierung deaktiviert werden.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.jobsuche.api_client import ApiClient
from deutschland.jobsuche.api_client import Endpoint as _Endpoint
from deutschland.jobsuche.model.job_details import JobDetails
from deutschland.jobsuche.model.job_search_response import JobSearchResponse
from deutschland.jobsuche.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ed_v1_arbeitgeberlogo_hash_id_get_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["clientCredAuth"],
                "endpoint_path": "/ed/v1/arbeitgeberlogo/{hashID}",
                "operation_id": "ed_v1_arbeitgeberlogo_hash_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "hash_id",
                ],
                "required": [
                    "hash_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "hash_id": (str,),
                },
                "attribute_map": {
                    "hash_id": "hashID",
                },
                "location_map": {
                    "hash_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["image/png"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.pc_v2_jobdetails_hash_id_get_endpoint = _Endpoint(
            settings={
                "response_type": (JobDetails,),
                "auth": ["clientCredAuth"],
                "endpoint_path": "/pc/v2/jobdetails/{hashID}",
                "operation_id": "pc_v2_jobdetails_hash_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "hash_id",
                ],
                "required": [
                    "hash_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "hash_id": (str,),
                },
                "attribute_map": {
                    "hash_id": "hashID",
                },
                "location_map": {
                    "hash_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.pc_v4_app_jobs_get_endpoint = _Endpoint(
            settings={
                "response_type": (JobSearchResponse,),
                "auth": ["clientCredAuth"],
                "endpoint_path": "/pc/v4/app/jobs",
                "operation_id": "pc_v4_app_jobs_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "was",
                    "wo",
                    "berufsfeld",
                    "page",
                    "size",
                    "arbeitgeber",
                    "veroeffentlichtseit",
                    "zeitarbeit",
                    "angebotsart",
                    "befristung",
                    "arbeitszeit",
                    "behinderung",
                    "corona",
                    "umkreis",
                ],
                "required": [],
                "nullable": [],
                "enum": [
                    "angebotsart",
                    "befristung",
                    "arbeitszeit",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("angebotsart",): {"1": 1, "2": 2, "4": 4, "34": 34},
                    ("befristung",): {"1": 1, "2": 2},
                    ("arbeitszeit",): {
                        "VZ": "vz",
                        "TZ": "tz",
                        "SNW": "snw",
                        "HO": "ho",
                        "MJ": "mj",
                    },
                },
                "openapi_types": {
                    "was": (str,),
                    "wo": (str,),
                    "berufsfeld": (str,),
                    "page": (int,),
                    "size": (int,),
                    "arbeitgeber": (str,),
                    "veroeffentlichtseit": (int,),
                    "zeitarbeit": (bool,),
                    "angebotsart": (int,),
                    "befristung": (int,),
                    "arbeitszeit": (str,),
                    "behinderung": (bool,),
                    "corona": (bool,),
                    "umkreis": (int,),
                },
                "attribute_map": {
                    "was": "was",
                    "wo": "wo",
                    "berufsfeld": "berufsfeld",
                    "page": "page",
                    "size": "size",
                    "arbeitgeber": "arbeitgeber",
                    "veroeffentlichtseit": "veroeffentlichtseit",
                    "zeitarbeit": "zeitarbeit",
                    "angebotsart": "angebotsart",
                    "befristung": "befristung",
                    "arbeitszeit": "arbeitszeit",
                    "behinderung": "behinderung",
                    "corona": "corona",
                    "umkreis": "umkreis",
                },
                "location_map": {
                    "was": "query",
                    "wo": "query",
                    "berufsfeld": "query",
                    "page": "query",
                    "size": "query",
                    "arbeitgeber": "query",
                    "veroeffentlichtseit": "query",
                    "zeitarbeit": "query",
                    "angebotsart": "query",
                    "befristung": "query",
                    "arbeitszeit": "query",
                    "behinderung": "query",
                    "corona": "query",
                    "umkreis": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def ed_v1_arbeitgeberlogo_hash_id_get(self, hash_id, **kwargs):
        """Unternehmen Logo  # noqa: E501

        Abrufen des Logos eines Unternehmens  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ed_v1_arbeitgeberlogo_hash_id_get(hash_id, async_req=True)
        >>> result = thread.get()

        Args:
            hash_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["hash_id"] = hash_id
        return self.ed_v1_arbeitgeberlogo_hash_id_get_endpoint.call_with_http_info(
            **kwargs
        )

    def pc_v2_jobdetails_hash_id_get(self, hash_id, **kwargs):
        """Jobdetail  # noqa: E501

        Abrufen von Details zu einem Job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pc_v2_jobdetails_hash_id_get(hash_id, async_req=True)
        >>> result = thread.get()

        Args:
            hash_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JobDetails
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["hash_id"] = hash_id
        return self.pc_v2_jobdetails_hash_id_get_endpoint.call_with_http_info(**kwargs)

    def pc_v4_app_jobs_get(self, **kwargs):
        """Jobsuche  # noqa: E501

        Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pc_v4_app_jobs_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            was (str): Freitext suche Jobtitel. [optional]
            wo (str): Freitext suche Beschäftigungsort. [optional]
            berufsfeld (str): Freitext suche Berufsfeld. [optional]
            page (int): Ergebnissseite. [optional]
            size (int): Anzahl von Ergebnissen. [optional]
            arbeitgeber (str): Arbeitgeber der Stelle. [optional]
            veroeffentlichtseit (int): Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen.. [optional]
            zeitarbeit (bool): Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true).. [optional]
            angebotsart (int): 1=ARBEIT; 2=SELBSTAENDIGKEIT, 4=AUSBILDUNG/Duales Studium, 34=Praktikum/Trainee. [optional]
            befristung (int): Semikolon-separierte mehrere Werte möglich (z.B. befristung=1;2) 1 = befristet; 2 = unbefristet. [optional]
            arbeitszeit (str): Semikolon-separierte mehrere Werte möglich (z.B. arbeitszeit=vz;tz) vz=VOLLZEIT, tz=TEILZEIT, snw=SCHICHT_NACHTARBEIT_WOCHENENDE, ho=HEIM_TELEARBEIT, mj=MINIJOB. [optional]
            behinderung (bool): [optional]
            corona (bool): Wenn true, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt.. [optional]
            umkreis (int): Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JobSearchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.pc_v4_app_jobs_get_endpoint.call_with_http_info(**kwargs)

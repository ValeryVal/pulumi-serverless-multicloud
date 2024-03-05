import json
from pathlib import Path
home = str(Path.home())
path_to_azure = home+"\.azure"
path_to_msal = path_to_azure+"\msal_token_cache.json"
path_to_sls = path_to_azure+"\slsTokenCache.json"
print(f"{path_to_sls=}")
tenant_id = "036e98fc-1d42-4ea1-9d0b-50bedbfb079c"


def get_account_numbers(json_data):
    access_account_number = filter_access_token_by_tenant_id(json_data, get_all_keys(json_data["AccessToken"]))
    refresh_account_number = filter_refresh_token_by_target(json_data)
    return access_account_number, refresh_account_number

def get_all_keys(dict_from_json):
    account_field_keys = []
    for key in dict_from_json.keys():
        account_field_keys.append(key)
    return account_field_keys


def filter_access_token_by_tenant_id(json_data, keys_to_filter):
    try:
        for key in keys_to_filter:
            if json_data["AccessToken"][key]['realm'] == tenant_id:
                return json_data["AccessToken"][key]['secret']
    except KeyError:
        pass


def filter_refresh_token_by_target(json_data):
    try:
        for key in json_data["RefreshToken"]:
            if json_data["RefreshToken"][key]['target'] == "https://management.core.windows.net//user_impersonation https://management.core.windows.net//.default":
                return json_data["RefreshToken"][key]['secret']
    except KeyError:
        pass


with open(path_to_msal, "r") as msal:
    msal_data = json.load(msal)
    access_token, refresh_token = get_account_numbers(msal_data)
    print(f"{access_token=}")
    print(f"{refresh_token=}")

with open(path_to_sls, "r") as sls:
    sls_data = json.load(sls)

with open(path_to_sls, "w") as sls:
    sls_data["entries"][0]["accessToken"] = access_token
    sls_data["entries"][0]["refreshToken"] = refresh_token
    sls_data["entries"][0]["tenantId"] = tenant_id
    json.dump(sls_data, sls)



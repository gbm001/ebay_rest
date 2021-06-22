# -*- coding: utf-8 -*-
"""
Copyright 2019 eBay Inc.

Licensed under the Apache License, Version 2.0 (the "License");
You may not use this file except in compliance with the License.
You may obtain a copy of the License at
    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.
"""
import json
import logging
from .model.model import Environment, Credentials


user_config_ids = ["sandbox-user", "production-user"]


class CredentialUtil():
    """
    credential_list: dictionary key=string, value=credentials
    """
    _credential_list = {}

    def load(self, app_config_path):
        logging.debug("Loading credential configuration file at: %s", app_config_path)
        with open(app_config_path, 'r') as f:
            if app_config_path.endswith('.json'):
                content = json.loads(f.read())
            else:
                raise ValueError('Configuration file need to be in JSON.')
            self._iterate(content)

    def _iterate(self, content):
        for key in content:
            logging.debug("Environment attempted: %s", key)

            if key in [Environment.PRODUCTION.config_id, Environment.SANDBOX.config_id]:
                client_id = content[key]['appid']
                dev_id = content[key]['devid']
                client_secret = content[key]['certid']
                ru_name = content[key]['redirecturi']

                app_info = Credentials(client_id, client_secret, dev_id, ru_name)
                self._credential_list.update({key: app_info})

    def get_credentials(self, env_type):
        """
        env_config_id: environment.PRODUCTION.config_id or environment.SANDBOX.config_id
        """
        if len(self._credential_list) == 0:
            msg = "No environment loaded from configuration file"
            logging.error(msg)
            raise CredentialNotLoadedError(msg)
        return self._credential_list[env_type.config_id]

    def update_credentials(self, sandbox: bool, credentials: Credentials):
        """
        Directly update the list of credentials.

        :param
        sandbox (bool): {True, False} For the sandbox True, for production False.

        :param
        credentials (Credentials): A Credentials instance.
        """
        key = Environment.SANDBOX.config_id if sandbox else Environment.PRODUCTION.config_id
        self._credential_list.update({key: credentials})


class CredentialNotLoadedError(Exception):
    pass

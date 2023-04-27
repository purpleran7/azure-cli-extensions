# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "workloads monitor provider-instance show",
    is_preview=True,
)
class Show(AAZCommand):
    """Show properties of a provider instance for the specified subscription, resource group, SAP monitor name, and resource name.

    :example: Show properties of a provider instance for the specified subscription, resource group, SAP monitor name, and resource name.
        az workloads monitor provider-instance show --monitor-name <monitor-name> -n <provider-instance-name> -g <RG-NAME>
    """

    _aaz_info = {
        "version": "2023-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/monitors/{}/providerinstances/{}", "2023-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Name of the SAP monitor resource.",
            required=True,
            id_part="name",
        )
        _args_schema.provider_instance_name = AAZStrArg(
            options=["-n", "--name", "--provider-instance-name"],
            help="Name of the provider instance.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ProviderInstancesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ProviderInstancesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/monitors/{monitorName}/providerInstances/{providerInstanceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerInstanceName", self.ctx.args.provider_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.errors = AAZObjectType()
            _ShowHelper._build_schema_error_read(properties.errors)
            properties.provider_settings = AAZObjectType(
                serialized_name="providerSettings",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            provider_settings = cls._schema_on_200.properties.provider_settings
            provider_settings.provider_type = AAZStrType(
                serialized_name="providerType",
                flags={"required": True},
            )

            disc_db2 = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "Db2")
            disc_db2.db_name = AAZStrType(
                serialized_name="dbName",
            )
            disc_db2.db_password = AAZStrType(
                serialized_name="dbPassword",
            )
            disc_db2.db_password_uri = AAZStrType(
                serialized_name="dbPasswordUri",
            )
            disc_db2.db_port = AAZStrType(
                serialized_name="dbPort",
            )
            disc_db2.db_username = AAZStrType(
                serialized_name="dbUsername",
            )
            disc_db2.hostname = AAZStrType()
            disc_db2.sap_sid = AAZStrType(
                serialized_name="sapSid",
            )
            disc_db2.ssl_certificate_uri = AAZStrType(
                serialized_name="sslCertificateUri",
            )
            disc_db2.ssl_preference = AAZStrType(
                serialized_name="sslPreference",
            )

            disc_ms_sql_server = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "MsSqlServer")
            disc_ms_sql_server.db_password = AAZStrType(
                serialized_name="dbPassword",
            )
            disc_ms_sql_server.db_password_uri = AAZStrType(
                serialized_name="dbPasswordUri",
            )
            disc_ms_sql_server.db_port = AAZStrType(
                serialized_name="dbPort",
            )
            disc_ms_sql_server.db_username = AAZStrType(
                serialized_name="dbUsername",
            )
            disc_ms_sql_server.hostname = AAZStrType()
            disc_ms_sql_server.sap_sid = AAZStrType(
                serialized_name="sapSid",
            )
            disc_ms_sql_server.ssl_certificate_uri = AAZStrType(
                serialized_name="sslCertificateUri",
            )
            disc_ms_sql_server.ssl_preference = AAZStrType(
                serialized_name="sslPreference",
            )

            disc_prometheus_ha_cluster = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "PrometheusHaCluster")
            disc_prometheus_ha_cluster.cluster_name = AAZStrType(
                serialized_name="clusterName",
            )
            disc_prometheus_ha_cluster.hostname = AAZStrType()
            disc_prometheus_ha_cluster.prometheus_url = AAZStrType(
                serialized_name="prometheusUrl",
            )
            disc_prometheus_ha_cluster.sid = AAZStrType()
            disc_prometheus_ha_cluster.ssl_certificate_uri = AAZStrType(
                serialized_name="sslCertificateUri",
            )
            disc_prometheus_ha_cluster.ssl_preference = AAZStrType(
                serialized_name="sslPreference",
            )

            disc_prometheus_os = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "PrometheusOS")
            disc_prometheus_os.prometheus_url = AAZStrType(
                serialized_name="prometheusUrl",
            )
            disc_prometheus_os.sap_sid = AAZStrType(
                serialized_name="sapSid",
            )
            disc_prometheus_os.ssl_certificate_uri = AAZStrType(
                serialized_name="sslCertificateUri",
            )
            disc_prometheus_os.ssl_preference = AAZStrType(
                serialized_name="sslPreference",
            )

            disc_sap_hana = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "SapHana")
            disc_sap_hana.db_name = AAZStrType(
                serialized_name="dbName",
            )
            disc_sap_hana.db_password = AAZStrType(
                serialized_name="dbPassword",
            )
            disc_sap_hana.db_password_uri = AAZStrType(
                serialized_name="dbPasswordUri",
            )
            disc_sap_hana.db_username = AAZStrType(
                serialized_name="dbUsername",
            )
            disc_sap_hana.hostname = AAZStrType()
            disc_sap_hana.instance_number = AAZStrType(
                serialized_name="instanceNumber",
            )
            disc_sap_hana.sap_sid = AAZStrType(
                serialized_name="sapSid",
            )
            disc_sap_hana.sql_port = AAZStrType(
                serialized_name="sqlPort",
            )
            disc_sap_hana.ssl_certificate_uri = AAZStrType(
                serialized_name="sslCertificateUri",
            )
            disc_sap_hana.ssl_host_name_in_certificate = AAZStrType(
                serialized_name="sslHostNameInCertificate",
            )
            disc_sap_hana.ssl_preference = AAZStrType(
                serialized_name="sslPreference",
            )

            disc_sap_net_weaver = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "SapNetWeaver")
            disc_sap_net_weaver.sap_client_id = AAZStrType(
                serialized_name="sapClientId",
            )
            disc_sap_net_weaver.sap_host_file_entries = AAZListType(
                serialized_name="sapHostFileEntries",
            )
            disc_sap_net_weaver.sap_hostname = AAZStrType(
                serialized_name="sapHostname",
            )
            disc_sap_net_weaver.sap_instance_nr = AAZStrType(
                serialized_name="sapInstanceNr",
            )
            disc_sap_net_weaver.sap_password = AAZStrType(
                serialized_name="sapPassword",
            )
            disc_sap_net_weaver.sap_password_uri = AAZStrType(
                serialized_name="sapPasswordUri",
            )
            disc_sap_net_weaver.sap_port_number = AAZStrType(
                serialized_name="sapPortNumber",
            )
            disc_sap_net_weaver.sap_sid = AAZStrType(
                serialized_name="sapSid",
            )
            disc_sap_net_weaver.sap_username = AAZStrType(
                serialized_name="sapUsername",
            )
            disc_sap_net_weaver.ssl_certificate_uri = AAZStrType(
                serialized_name="sslCertificateUri",
            )
            disc_sap_net_weaver.ssl_preference = AAZStrType(
                serialized_name="sslPreference",
            )

            sap_host_file_entries = cls._schema_on_200.properties.provider_settings.discriminate_by("provider_type", "SapNetWeaver").sap_host_file_entries
            sap_host_file_entries.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_error_read = None

    @classmethod
    def _build_schema_error_read(cls, _schema):
        if cls._schema_error_read is not None:
            _schema.code = cls._schema_error_read.code
            _schema.details = cls._schema_error_read.details
            _schema.inner_error = cls._schema_error_read.inner_error
            _schema.message = cls._schema_error_read.message
            _schema.target = cls._schema_error_read.target
            return

        cls._schema_error_read = _schema_error_read = AAZObjectType()

        error_read = _schema_error_read
        error_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_read.inner_error = AAZObjectType(
            serialized_name="innerError",
            flags={"read_only": True},
        )
        error_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_read.target = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_read(details.Element)

        inner_error = _schema_error_read.inner_error
        inner_error.inner_error = AAZObjectType(
            serialized_name="innerError",
        )
        cls._build_schema_error_read(inner_error.inner_error)

        _schema.code = cls._schema_error_read.code
        _schema.details = cls._schema_error_read.details
        _schema.inner_error = cls._schema_error_read.inner_error
        _schema.message = cls._schema_error_read.message
        _schema.target = cls._schema_error_read.target


__all__ = ["Show"]

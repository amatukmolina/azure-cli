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
    "network public-ip prefix update",
)
class Update(AAZCommand):
    """Update a public IP prefix resource.

    :example: Update a public IP prefix resource. (autogenerated)
        az network public-ip prefix update --name MyPublicIPPrefix --resource-group MyResourceGroup --set useRemoteGateways=true
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/publicipprefixes/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the public IP prefix.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ExtendedLocation"

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.PublicIPPrefixesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.PublicIPPrefixesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PublicIPPrefixesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "publicIpPrefixName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
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
            _UpdateHelper._build_schema_public_ip_prefix_read(cls._schema_on_200)

            return cls._schema_on_200

    class PublicIPPrefixesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "publicIpPrefixName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_public_ip_prefix_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("extendedLocation", AAZObjectType)
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_public_ip_prefix_read = None

    @classmethod
    def _build_schema_public_ip_prefix_read(cls, _schema):
        if cls._schema_public_ip_prefix_read is not None:
            _schema.etag = cls._schema_public_ip_prefix_read.etag
            _schema.extended_location = cls._schema_public_ip_prefix_read.extended_location
            _schema.id = cls._schema_public_ip_prefix_read.id
            _schema.location = cls._schema_public_ip_prefix_read.location
            _schema.name = cls._schema_public_ip_prefix_read.name
            _schema.properties = cls._schema_public_ip_prefix_read.properties
            _schema.sku = cls._schema_public_ip_prefix_read.sku
            _schema.tags = cls._schema_public_ip_prefix_read.tags
            _schema.type = cls._schema_public_ip_prefix_read.type
            _schema.zones = cls._schema_public_ip_prefix_read.zones
            return

        cls._schema_public_ip_prefix_read = _schema_public_ip_prefix_read = AAZObjectType()

        public_ip_prefix_read = _schema_public_ip_prefix_read
        public_ip_prefix_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        public_ip_prefix_read.extended_location = AAZObjectType(
            serialized_name="extendedLocation",
        )
        public_ip_prefix_read.id = AAZStrType()
        public_ip_prefix_read.location = AAZStrType()
        public_ip_prefix_read.name = AAZStrType(
            flags={"read_only": True},
        )
        public_ip_prefix_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        public_ip_prefix_read.sku = AAZObjectType()
        public_ip_prefix_read.tags = AAZDictType()
        public_ip_prefix_read.type = AAZStrType(
            flags={"read_only": True},
        )
        public_ip_prefix_read.zones = AAZListType()

        extended_location = _schema_public_ip_prefix_read.extended_location
        extended_location.name = AAZStrType()
        extended_location.type = AAZStrType()

        properties = _schema_public_ip_prefix_read.properties
        properties.custom_ip_prefix = AAZObjectType(
            serialized_name="customIPPrefix",
        )
        cls._build_schema_sub_resource_read(properties.custom_ip_prefix)
        properties.ip_prefix = AAZStrType(
            serialized_name="ipPrefix",
            flags={"read_only": True},
        )
        properties.ip_tags = AAZListType(
            serialized_name="ipTags",
        )
        properties.load_balancer_frontend_ip_configuration = AAZObjectType(
            serialized_name="loadBalancerFrontendIpConfiguration",
        )
        cls._build_schema_sub_resource_read(properties.load_balancer_frontend_ip_configuration)
        properties.nat_gateway = AAZObjectType(
            serialized_name="natGateway",
        )
        properties.prefix_length = AAZIntType(
            serialized_name="prefixLength",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_address_version = AAZStrType(
            serialized_name="publicIPAddressVersion",
        )
        properties.public_ip_addresses = AAZListType(
            serialized_name="publicIPAddresses",
            flags={"read_only": True},
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )

        ip_tags = _schema_public_ip_prefix_read.properties.ip_tags
        ip_tags.Element = AAZObjectType()

        _element = _schema_public_ip_prefix_read.properties.ip_tags.Element
        _element.ip_tag_type = AAZStrType(
            serialized_name="ipTagType",
        )
        _element.tag = AAZStrType()

        nat_gateway = _schema_public_ip_prefix_read.properties.nat_gateway
        nat_gateway.etag = AAZStrType(
            flags={"read_only": True},
        )
        nat_gateway.id = AAZStrType()
        nat_gateway.location = AAZStrType()
        nat_gateway.name = AAZStrType(
            flags={"read_only": True},
        )
        nat_gateway.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        nat_gateway.sku = AAZObjectType()
        nat_gateway.tags = AAZDictType()
        nat_gateway.type = AAZStrType(
            flags={"read_only": True},
        )
        nat_gateway.zones = AAZListType()

        properties = _schema_public_ip_prefix_read.properties.nat_gateway.properties
        properties.idle_timeout_in_minutes = AAZIntType(
            serialized_name="idleTimeoutInMinutes",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_addresses = AAZListType(
            serialized_name="publicIpAddresses",
        )
        properties.public_ip_prefixes = AAZListType(
            serialized_name="publicIpPrefixes",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )
        properties.subnets = AAZListType(
            flags={"read_only": True},
        )

        public_ip_addresses = _schema_public_ip_prefix_read.properties.nat_gateway.properties.public_ip_addresses
        public_ip_addresses.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(public_ip_addresses.Element)

        public_ip_prefixes = _schema_public_ip_prefix_read.properties.nat_gateway.properties.public_ip_prefixes
        public_ip_prefixes.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(public_ip_prefixes.Element)

        subnets = _schema_public_ip_prefix_read.properties.nat_gateway.properties.subnets
        subnets.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(subnets.Element)

        sku = _schema_public_ip_prefix_read.properties.nat_gateway.sku
        sku.name = AAZStrType()

        tags = _schema_public_ip_prefix_read.properties.nat_gateway.tags
        tags.Element = AAZStrType()

        zones = _schema_public_ip_prefix_read.properties.nat_gateway.zones
        zones.Element = AAZStrType()

        public_ip_addresses = _schema_public_ip_prefix_read.properties.public_ip_addresses
        public_ip_addresses.Element = AAZObjectType()

        _element = _schema_public_ip_prefix_read.properties.public_ip_addresses.Element
        _element.id = AAZStrType()

        sku = _schema_public_ip_prefix_read.sku
        sku.name = AAZStrType()
        sku.tier = AAZStrType()

        tags = _schema_public_ip_prefix_read.tags
        tags.Element = AAZStrType()

        zones = _schema_public_ip_prefix_read.zones
        zones.Element = AAZStrType()

        _schema.etag = cls._schema_public_ip_prefix_read.etag
        _schema.extended_location = cls._schema_public_ip_prefix_read.extended_location
        _schema.id = cls._schema_public_ip_prefix_read.id
        _schema.location = cls._schema_public_ip_prefix_read.location
        _schema.name = cls._schema_public_ip_prefix_read.name
        _schema.properties = cls._schema_public_ip_prefix_read.properties
        _schema.sku = cls._schema_public_ip_prefix_read.sku
        _schema.tags = cls._schema_public_ip_prefix_read.tags
        _schema.type = cls._schema_public_ip_prefix_read.type
        _schema.zones = cls._schema_public_ip_prefix_read.zones

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
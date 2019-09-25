from rest_framework.serializers import ModelSerializer

from .models import (
    Address,
    Animal_Risk_Factor,
    Association_Membership,
    Inspection_Report,
    Operation_Risk_Factor,
    Operator,
    Registration,
    Renewal,
)


class Address_Serializer(ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "address_type",
            "street_num",
            "suite",
            "street_name",
            "POBox",
            "city",
            "postal_code",
            "region",
        )


class Association_Membership_Serializer(ModelSerializer):
    class Meta:
        model = Association_Membership
        fields = ("id", "assoc_name")


class Operation_Risk_Factor_Serializer(ModelSerializer):
    class Meta:
        model = Operation_Risk_Factor
        fields = (
            "id",
            "accidental_breeding",
            "num_workers",
            "has_vet",
            "has_perm_id",
            "perm_id_type",
            "perm_id_other",
        )


class Animal_Risk_Factor_Serializer(ModelSerializer):
    class Meta:
        model = Animal_Risk_Factor
        fields = (
            "id",
            "animal_type",
            "num_breeds",
            "num_females_intact",
            "num_litter",
            "num_sold",
            "num_transferred",
            "num_traded",
            "num_leased",
            "num_animals",
        )


class Operator_Serializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "comm_pref",
            "phone_num",
            "email_address",
            "operation_type",
            "operation_name",
            "operation_URL",
            "comm_pref",
        )


class Renewal_Serializer(ModelSerializer):
    class Meta:
        model = Renewal
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "previous_registration_number",
        )


class Registration_Serializer(ModelSerializer):
    operator = Operator_Serializer()
    addresses = Address_Serializer(many=True)
    associations = Association_Membership_Serializer(many=True)
    animal_risk_factors = Animal_Risk_Factor_Serializer(many=True)
    operation_risk_factors = Operation_Risk_Factor_Serializer(many=True)
    renewals = Renewal_Serializer(many=True)

    class Meta:
        model = Registration
        fields = (
            "id",
            "operator_status",
            "registration_number",
            "registration_date",
            "num_locations",
            "operator",
            "addresses",
            "associations",
            "animal_risk_factors",
            "operation_risk_factors",
            "renewals",
        )

    def create(self, validated_data):
        operator_data = validated_data.pop("operator")
        animals_data = validated_data.pop("animal_risk_factors")
        associations_data = validated_data.pop("associations")
        addresses_data = validated_data.pop("addresses")
        operations_data = validated_data.pop("operation_risk_factors")
        renewals_data = validated_data.pop("renewals")

        registration = Registration.objects.create(**validated_data)

        for address_data in addresses_data:
            Address.objects.create(registration_number=registration, **address_data)
            registration.num_locations += 1

        for association_data in associations_data:
            Association_Membership.objects.create(
                registration_number=registration, **association_data
            )
        for animal_data in animals_data:
            Animal_Risk_Factor.objects.create(
                registration_number=registration, **animal_data
            )

        for operation_data in operations_data:
            Operation_Risk_Factor.objects.create(
                registration_number=registration, **operation_data
            )
        for renewal_data in renewals_data:
            Renewal.objects.create(registration_number=registration, **renewal_data)

        Operator.objects.create(registration_number=registration, **operator_data)

        return registration


class Inspection_Report_Serializer(ModelSerializer):
    class Meta:
        model = Inspection_Report
        fields = "__all__"

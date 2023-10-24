# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci


# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info


def get_config(user_ocid, private_key_file, fingerprint, tenancy_ocid, region):
    config = {
        "user": user_ocid,
        "key_file": private_key_file,
        "fingerprint": fingerprint,
        "tenancy": tenancy_ocid,
        "region": region
    }
    return config


def oci_vm_start_stop(core_client, instance_id, action):
    # Send the request to service, some parameters are not required, see API
    # doc for more info
    if action in ("start", "START", "stop", "STOP"):
        instance_action_response = core_client.instance_action(
            instance_id=instance_id,
            action=action,
            # opc_retry_token="EXAMPLE-opcRetryToken-Value",
            # if_match="EXAMPLE-ifMatch-Value",
            # instance_power_action_details=oci.core.models.ResetActionDetails(
            #     action_type="reset",
            #     allow_dense_reboot_migration=False)
        )

        # Get the data from response
        print(instance_action_response.data)
    else:
        raise Exception(f"instance {action} failed")


def handler(user_ocid, private_key_file, fingerprint, tenancy_ocid, region, instance_id, action):
    # user_ocid, private_key_file, fingerprint, tenancy_ocid, region
    config = get_config(user_ocid, private_key_file, fingerprint, tenancy_ocid, region)
    core_client = oci.core.ComputeClient(config)
    # instance_id, action
    oci_vm_start_stop(core_client, instance_id, action)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     oci_vm_start_stop('ocid1.instance.oc1.ap-seoul-1.anuwgljrzwnc6yacvbjwzp5dglfcsovrd3s5vjlcp2bgq4j', 'd')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

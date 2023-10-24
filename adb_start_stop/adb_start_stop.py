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
config = oci.config.from_file()

# Initialize service client with default config file
database_client = oci.database.DatabaseClient(config)


def oci_adb_start_stop(autonomous_database_id, action):
    if action in ('start', 'START'):
        # Send the request to service, some parameters are not required, see API
        # doc for more info
        start_autonomous_database_response = database_client.start_autonomous_database(
            autonomous_database_id=autonomous_database_id,
            # if_match="EXAMPLE-ifMatch-Value"
        )

        # Get the data from response
        print(start_autonomous_database_response.data)
    elif action in ('stop', 'STOP'):
        stop_autonomous_database_response = database_client.stop_autonomous_database(
            autonomous_database_id=autonomous_database_id,
            # if_match="EXAMPLE-ifMatch-Value",
            # opc_request_id="EFJURXMI7CTLLHZWT2SY<unique_ID>"
        )

        # Get the data from response
        print(stop_autonomous_database_response.data)
    else:
        raise Exception(f"instance {action} failed")


# if __name__ == '__main__':
#     oci_adb_start_stop('ocid1.autonomousdatabase.oc1.ap-seoul-1.anuwgljrzwnc6yaa3fmxo4swxmtu7pezrzfry2iwua5', 'START')

from google.cloud import spanner
def insert_msgs_dml(instance_id, database_id):

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_msgs(transaction):
        row_ct = transaction.execute_update(
            "INSERT message (mesg, time) "
            " VALUES ('Hello GCP', '2022-03-10 10:10:53.163')"
        )

        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(insert_msgs)

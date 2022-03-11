from google.cloud import spanner

import random 

import string 

import time

    

def rand_value(size): 

    generate_pass = ''.join([random.choice( 

                        string.ascii_lowercase) 

                        for n in range(size)]) 

                            

    return generate_pass   

def rand_time():

    generate_time = random.randint(1,60)

    return generate_time



while True:

    stringvalue=rand_value(10)

    print(stringvalue)

    instance_id = "first-instance1"

    database_id = "exampledb"

    spanner_client = spanner.Client()

    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    def insert_msg(transaction):

        row_ct = transaction.execute_update(
            "INSERT message (mesg, time) VALUES "
        "('" + stringvalue + "', CURRENT_TIMESTAMP())"
        )

        print("{} record(s) inserted.".format(row_ct)) 

    database.run_in_transaction(insert_msg)

    sleep_time = rand_time()

    print(sleep_time)

    time.sleep(sleep_time)
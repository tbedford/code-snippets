## NOTE: this assumes you have a timestamp as the first column in your CSV data
# pip install quixstreams
import quixstreams as qx
import time
import datetime
import os
import pandas as pd
from dotenv import load_dotenv

def main():
    load_dotenv()
    token = os.getenv("SDK_TOKEN")

    csv_file = "users.csv"
    users = pd.read_csv(csv_file)

    # Obtain client library token from portal
    client = qx.QuixStreamingClient(token)

    # Open a topic to publish data to
    topic_producer = client.get_topic_producer("quickstart-users-streams")
    stream = topic_producer.create_stream()
    stream.properties.name = "Quickstart CSV using Streams"
    print('Writing CSV data to stream...')
    stream.timeseries.publish(users)
    print("Closing stream")
    stream.close()

if __name__ == '__main__':
    main()

    

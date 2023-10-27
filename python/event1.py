import quixstreams as qx
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("STREAMING_TOKEN")

# Obtain client library token from portal
client = qx.QuixStreamingClient(token)
#client.api_url = "https://portal-api.dev.quix.ai"

# Open a topic to publish data to. Topic is created if it does not exist.
topic_producer = client.get_topic_producer("events")

stream = topic_producer.create_stream()
stream.properties.name = "Machine Events"
stream.timeseries.buffer.time_span_in_milliseconds = 100   # Send data in 100 ms chunks

def main():
    try:
        while True:
            print("UP event")
            stream.events \
                .add_timestamp(datetime.datetime.utcnow()) \
                .add_value("MachineState", "UP") \
                .publish()
            print("sleeping...")
            time.sleep(3)
            print("DOWN event")
            stream.events \
                .add_timestamp(datetime.datetime.utcnow()) \
                .add_value("MachineState", "DOWN") \
                .publish()
            time.sleep(3)            
    except KeyboardInterrupt:
        print("Closing stream")
        stream.close()

if __name__ == '__main__':
    main()

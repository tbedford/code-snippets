import os
from quixstreams import Application, State
from quixstreams.models.serializers.quix import JSONDeserializer, QuixTimeseriesSerializer
from datetime import timedelta

def my_func(row):
    if 'Number' in row:
        # print(row['Number'])
        return row['Number']
    return 0

app = Application.Quix("transformation-v1", auto_offset_reset="earliest")
input_topic = app.topic(os.environ["input"], value_deserializer=JSONDeserializer())
output_topic = app.topic(os.environ["output"], value_serializer=QuixTimeseriesSerializer())

sdf = app.dataframe(input_topic)
sdf = sdf.filter(lambda row: 'Number' in row)

sdf = (
    # Extract the "total" field from the record
    sdf.apply(my_func)

    # Define a tumbling window of 10 minutes
    .tumbling_window(timedelta(seconds=10))

    # Specify the "sum" aggregation function to apply to values of "total"
    .mean()

    # Emit results only when the 10 minute window has elapsed
    .final()
)

sdf = sdf.update(lambda value: print(value))

if __name__ == "__main__":
    app.run(sdf)

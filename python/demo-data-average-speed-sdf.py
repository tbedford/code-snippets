import os
from quixstreams import Application, State
from quixstreams.models.serializers.quix import QuixDeserializer, JSONSerializer
from datetime import timedelta

def my_func(row):
    #print('my_func')
    if 'Speed' in row:
        if row['Speed'] != None:
            #print('Speed is -> ', row['Speed'])
            return row['Speed']
        else:
            print('Speed is None')
            row['Speed'] = 0
            return row['Speed']
    else:
        print('no Speed in row')   
        return 0

def my_func2(row):
    return row['Speed']

app = Application.Quix("transformation-v2", auto_offset_reset="earliest")
input_topic = app.topic(os.environ["input"], value_deserializer=QuixDeserializer())
output_topic = app.topic(os.environ["output"], value_serializer=JSONSerializer())
sdf = app.dataframe(input_topic)

sdf = sdf.filter(lambda row: 'Speed' in row)
sdf = sdf.filter(lambda row: row['Speed'] != None)

sdf = (
    sdf.apply(my_func2)
    .tumbling_window(timedelta(seconds=10))
    .mean()
    .final()
)

sdf = sdf.update(lambda row: print(row))

sdf = sdf.to_topic(output_topic)

if __name__ == "__main__":
    app.run(sdf)

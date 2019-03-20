import tensorflow as tf
from flask import jsonify

def getWebResponse(payload):
    observations = payload['observations']
    return jsonify(
            status=200,
            payload=payload,
            result=run(observations)
        )

def run(observations):
    tf.reset_default_graph()

    with tf.Session() as sess:
        with tf.gfile.GFile('./siloRefill/frozen_graph_def.pb', "rb") as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())

        tf.import_graph_def(graph_def, name='')
        graph = tf.get_default_graph()

        x = graph.get_tensor_by_name('vector_observation:0')
        y = graph.get_tensor_by_name('value_estimate:0')

        result = str(sess.run(y, feed_dict={x: [observations]})[0][0])
        return result


#print(run([0.2727273, 0.690625, 0.03937501, -0.2727273, 0.0, 2.561667]))
#print(run([0.4055944, 0.675625, 0.324375, 0.1118881, 0.0, 1.801667]))
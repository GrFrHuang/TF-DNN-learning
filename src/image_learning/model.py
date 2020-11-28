import tensorflow as tf
import pandas as pd
import numpy

# Compatible with tf's old version for initial the runtime session
tf.compat.v1.disable_eager_execution()

v1 = tf.constant([1, 2, 3, 4])
v2 = tf.constant([2, 0, 4, 3])
vAdd = tf.add(v1, v2)

# initial histogram for output to summary directory
# loss = tf...
# tf.summary.scalar('loss',loss)

# initial tf session for operate variables
with tf.compat.v1.Session() as ses:
    print(ses.run(vAdd))

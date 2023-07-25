import tensorflow as tf

class Predictior:
    def __init__(self, forecasted, real):
        self.forecasted = tf.constant(forecasted, name='input')
        self.weight = tf.Variable(forecasted, name='weight')
        self.output = tf.mul(self.weight, self.forecasted, name='output')
        self.real = tf.constant(real, name='correct_value')
        self.loss = tf.pow(self.output - self.real, 2, name='loss')
        self.train_step = tf.train.GradientDescentOptimizer(0.025).minimize(self.loss)
        for value in [self.forecasted, self.weight , self.output, self.real, self.loss]:
            tf.scalar_summary(value.op.name, value)
        self.summaries = tf.merge_all_summaries()

    def train(self):
        sess = tf.Session()
        summary_writer = tf.train.SummaryWriter('stats/log_wind_stats', sess.graph)

        sess.run(tf.initialize_all_variables())
        for i in range(100):
            summary_writer.add_summary(sess.run(self.summaries), i)
            sess.run(self.train_step)
        return summary_writer
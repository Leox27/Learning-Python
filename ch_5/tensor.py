import tensorflow as tf

# 0D Tensor (Scalar)
scalar = tf.constant(250)
print("Scalar:", scalar)

# 1D Tensor (Vector)
vector = tf.constant([250, 200, 300])
print("Vector:", vector)

# 2D Tensor (Matrix)
matrix = tf.constant([[250, 200, 300],
                      [150, 100, 350]])
print("Matrix:\n", matrix)

# 3D Tensor
tensor3D = tf.constant([
  [[250, 200, 300], [150, 100, 350]],
  [[220, 180, 260], [170, 130, 300]]
])
print("3D Tensor:\n", tensor3D)

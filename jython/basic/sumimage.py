# @OpService ops
# @Dataset data

from net.imglib2.type.numeric.real import FloatType

print ops.stats().sum(FloatType(), data)
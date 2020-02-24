from ipykernel.kernelapp import IPKernelApp
from . import WhileKernel

IPKernelApp.launch_instance(kernel_class=WhileKernel)

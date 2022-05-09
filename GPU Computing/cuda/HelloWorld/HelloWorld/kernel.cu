#include <stdio.h>
#include <iostream>
#include <cuda_runtime.h>
#include "device_launch_parameters.h"
int main(void) {
	helloFromGpu <<<1, 10 >>>() ;
	cudaDeviceReset();
	
}

__global__ void helloFromGpu(void) {
	printf("thread id ");
	printf("hello from gpu");
}
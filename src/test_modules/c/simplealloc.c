#include <stdlib.h>

int main(void)
{
  void* alloc = malloc(1024);
  free(alloc);
}

#include <stdlib.h>

int main(void)
{
  void* alloc = malloc(1024000);
  free(alloc);
}

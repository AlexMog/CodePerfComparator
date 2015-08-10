int main(void)
{
  void* alloc = new char[1024000];
  delete[] alloc;
}

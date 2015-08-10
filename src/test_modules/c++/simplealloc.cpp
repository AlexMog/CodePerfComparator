int main(void)
{
  void* alloc = new char[1024];
  delete[] alloc;
}

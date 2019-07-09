from psutil import virtual_memory

bytes_per_gb = 1024*1024*1024

mem = virtual_memory()
mem.total  # total physical memory available

max_ram = mem.total
available_ram = mem.available
print(type(max_ram))

print("Total RAM: %0.2f Gb" % ((max_ram)/(bytes_per_gb)))
print("Avaliable RAM: %0.2f Gb" % (available_ram/bytes_per_gb))
max_block_size = 64 * 1024

object_count = int(available_ram / max_block_size)
print("object_count: %s" % str(object_count))

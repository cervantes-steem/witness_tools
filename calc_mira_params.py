__author__ = "http://steemit.com/@cervantes"
__copyright__ = "Copyright (C) 2019 steem's @cervantes"
__license__ = "MIT"
__version__ = "1.0"

from psutil import virtual_memory
import json
import resource
import subprocess
import os
import pwd
import sys


max_nr_of_open_files =  resource.getrlimit(resource.RLIMIT_NOFILE)[0]


'''
Example database.cfg

{
  "global": {
    "shared_cache": {
      "capacity": "5368709120"
    },
    "write_buffer_manager": {
      "write_buffer_size": "1073741824"
    },
    "object_count": 62500,
    "statistics": false
  },
  "base": {
    "optimize_level_style_compaction": true,
    "increase_parallelism": true,
    "block_based_table_options": {
      "block_size": 8192,
      "cache_index_and_filter_blocks": true,
      "bloom_filter_policy": {
        "bits_per_key": 10,
        "use_block_based_builder": false
      }
    }
  }
}

'''
bytes_per_gb = 1024*1024*1024
open_files_offset = 500
steemd_memory_need = 5.5 * bytes_per_gb
config_file_name = "database.cfg"

mem = virtual_memory()
mem.total  # total physical memory available

max_ram = mem.total
available_ram = mem.available
#print(type(max_ram))

print("Total RAM: %0.2f Gb" % ((max_ram)/(bytes_per_gb)))
print("Avaliable RAM: %0.2f Gb" % (available_ram/bytes_per_gb))
print("Average RAM needed for steemd process: %0.2f Gb" % (steemd_memory_need/bytes_per_gb))
max_block_size = 64 * 1024

if(available_ram<steemd_memory_need):
  print("\tYou can`t run 'steemd' on this host, you need to free at least %0.2f Gb RAM" % ((steemd_memory_need-available_ram)/bytes_per_gb))
  sys.exit()

object_count = int((available_ram-stemd_memory_usage) / max_block_size)
global_shared_capacity = int((available_ram-stemd_memory_usage) / 3)
write_buffer_size = 1073741824

config = dict()

config["global"] = {}
config["global"]["shared_cache"] = {"capacity": "%i" % global_shared_capacity}
config["global"]["write_buffer_manager"] = {"write_buffer_size": "%i" % write_buffer_size}
config["global"]["object_count"] = "%i" % object_count
config["global"]["statistics"] = False
config["base"] = {}
config["base"]["optimize_level_style_compaction"] = True
config["base"]["optimize_level_style_compaction"] = True
config["base"]["optimize_level_style_compaction"] = True
config["base"]["optimize_level_style_compaction"] = True
config["base"]["optimize_level_style_compaction"] = True


print("\tobject_count: %s" % str(object_count))
print("\tglobal_shared_capacity: %i" % global_shared_capacity)
print("\tmax_nr_of_open_files: %i" % max_nr_of_open_files)

if(object_count>max_nr_of_open_files):
  print("\nThe actual number of allowed open files (%i) is lower than the suggested object count (%i)!" % (max_nr_of_open_files, object_count))
  answer = input("\tDo you want to set the limit to %i (object_count increased by an offset of %s? (Y/N) " % (object_count + open_files_offset, open_files_offset))
  if(answer=="Y"):
    print("\tSetting open file limit to: %i ..." % (object_count + open_files_offset))
  else:
    print("\tPlease set the value manually with: $>ulimit -n %i" % (object_count + open_files_offset))

answer = input("\tDo you want to save mira configuration file to %s " % config_file_name)
if(answer=="Y"):
  print("Writting config file: '%s' with following calculated params...:\n" % config_file_name)
with open(config_file_name, 'w') as outfile:  
    json.dump(config, outfile, indent=4)






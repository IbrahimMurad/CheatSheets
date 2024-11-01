# Redis Commands Cheat Sheet

## 1. Basic Commands
| Command | Description |
| ------- | ----------- |
| `redis-cli` | Start the Redis command-line interface |
| `ping` | Check if the Redis server is running |
| `select <db_number>` | Select a specific database (default is 0) |
| `flushdb` | Remove all keys from the current database |
| `flushall` | Remove all keys from all databases |

## 2. Working with Keys
| Command | Description |
| ------- | ----------- |
| `set <key> <value>` | Set the value of a key |
| `get <key>` | Get the value of a key |
| `del <key>` | Delete a key |
| `exists <key>` | Check if a key exists |
| `expire <key> <seconds>` | Set a timeout on a key |
| `ttl <key>` | Get the time-to-live of a key |
| `keys <pattern>` | Find all keys matching a pattern |

## 3. Working with Strings
| Command | Description |
| ------- | ----------- |
| `set <key> <value>` | Set the value of a string key |
| `get <key>` | Get the value of a string key |
| `append <key> <value>` | Append a value to a string key |
| `strlen <key>` | Get the length of a string key |
| `incr <key>` | Increment the integer value of a key by one |
| `decr <key>` | Decrement the integer value of a key by one |

## 4. Working with Hashes
| Command | Description |
| ------- | ----------- |
| `hset <key> <field> <value>` | Set the value of a hash field |
| `hget <key> <field>` | Get the value of a hash field |
| `hdel <key> <field>` | Delete a hash field |
| `hgetall <key>` | Get all fields and values of a hash |
| `hexists <key> <field>` | Check if a hash field exists |
| `hlen <key>` | Get the number of fields in a hash |

## 5. Working with Lists
| Command | Description |
| ------- | ----------- |
| `lpush <key> <value>` | Prepend a value to a list |
| `rpush <key> <value>` | Append a value to a list |
| `lpop <key>` | Remove and get the first element of a list |
| `rpop <key>` | Remove and get the last element of a list |
| `lrange <key> <start> <stop>` | Get a range of elements from a list |
| `llen <key>` | Get the length of a list |

## 6. Working with Sets
| Command | Description |
| ------- | ----------- |
| `sadd <key> <member>` | Add a member to a set |
| `srem <key> <member>` | Remove a member from a set |
| `smembers <key>` | Get all members of a set |
| `sismember <key> <member>` | Check if a member exists in a set |
| `scard <key>` | Get the number of members in a set |

## 7. Working with Sorted Sets
| Command | Description |
| ------- | ----------- |
| `zadd <key> <score> <member>` | Add a member to a sorted set with a score |
| `zrem <key> <member>` | Remove a member from a sorted set |
| `zrange <key> <start> <stop>` | Get a range of members in a sorted set by index |
| `zrangebyscore <key> <min> <max>` | Get a range of members in a sorted set by score |
| `zscore <key> <member>` | Get the score of a member in a sorted set |
| `zcard <key>` | Get the number of members in a sorted set |

## 8. Transactions
| Command | Description |
| ------- | ----------- |
| `multi` | Start a transaction |
| `exec` | Execute a transaction |
| `discard` | Discard a transaction |
| `watch <key>` | Watch a key for changes (used with transactions) |
| `unwatch` | Unwatch all keys |

## 9. Pub/Sub
| Command | Description |
| ------- | ----------- |
| `publish <channel> <message>` | Publish a message to a channel |
| `subscribe <channel>` | Subscribe to a channel |
| `unsubscribe <channel>` | Unsubscribe from a channel |
| `psubscribe <pattern>` | Subscribe to channels matching a pattern |
| `punsubscribe <pattern>` | Unsubscribe from channels matching a pattern |

## 10. Scripting
| Command | Description |
| ------- | ----------- |
| `eval <script> <numkeys> <key> [<arg> ...]` | Execute a Lua script |
| `evalsha <sha1> <numkeys> <key> [<arg> ...]` | Execute a cached Lua script |
| `script load <script>` | Load a Lua script into the script cache |
| `script exists <sha1>` | Check if a script exists in the script cache |
| `script flush` | Remove all scripts from the script cache |

## 11. Server Management
| Command | Description |
| ------- | ----------- |
| `info` | Get information and statistics about the server |
| `config get <parameter>` | Get the value of a configuration parameter |
| `config set <parameter> <value>` | Set a configuration parameter |
| `config rewrite` | Rewrite the configuration file with the in-memory configuration |
| `save` | Synchronously save the dataset to disk |
| `bgsave` | Asynchronously save the dataset to disk |
| `shutdown` | Synchronously save the dataset to disk and then shut down the server |
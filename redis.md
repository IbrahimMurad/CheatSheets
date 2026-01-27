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
| `dbsize` | Get the number of keys in the current database |
| `lastsave` | Get the UNIX timestamp of the last successful save |

## 12. Persistence and Backup
| Command | Description |
| ------- | ----------- |
| `bgsave` | Create a snapshot in the background |
| `lastsave` | Get the timestamp of the last successful save |
| `save` | Synchronously save the dataset (blocks all clients) |
| `bgrewriteaof` | Rewrite the append-only file in the background |

## 13. Advanced Key Operations
| Command | Description |
| ------- | ----------- |
| `rename <key> <newkey>` | Rename a key |
| `renamenx <key> <newkey>` | Rename a key only if the new key doesn't exist |
| `type <key>` | Determine the type stored at a key |
| `persist <key>` | Remove the expiration from a key |
| `pexpire <key> <milliseconds>` | Set a key's time to live in milliseconds |
| `pttl <key>` | Get the time to live for a key in milliseconds |
| `scan <cursor> [MATCH pattern] [COUNT count]` | Incrementally iterate over keys |
| `dump <key>` | Serialize the value stored at a key |
| `restore <key> <ttl> <serialized-value>` | Create a key from a serialized value |

## 14. String Operations (Advanced)
| Command | Description |
| ------- | ----------- |
| `setex <key> <seconds> <value>` | Set key with expiration time in seconds |
| `setnx <key> <value>` | Set key only if it doesn't exist |
| `setrange <key> <offset> <value>` | Overwrite part of a string |
| `getrange <key> <start> <end>` | Get a substring of a string value |
| `mset <key1> <value1> <key2> <value2>` | Set multiple keys to multiple values |
| `mget <key1> <key2> ...` | Get the values of multiple keys |
| `incrby <key> <increment>` | Increment the value by a specified amount |
| `decrby <key> <decrement>` | Decrement the value by a specified amount |
| `incrbyfloat <key> <increment>` | Increment the float value by specified amount |

## 15. Hash Operations (Advanced)
| Command | Description |
| ------- | ----------- |
| `hmset <key> <field1> <value1> <field2> <value2>` | Set multiple hash fields to multiple values |
| `hmget <key> <field1> <field2>` | Get the values of multiple hash fields |
| `hincrby <key> <field> <increment>` | Increment the integer value of a hash field |
| `hincrbyfloat <key> <field> <increment>` | Increment the float value of a hash field |
| `hkeys <key>` | Get all the fields in a hash |
| `hvals <key>` | Get all the values in a hash |
| `hscan <key> <cursor>` | Incrementally iterate hash fields and values |

## 16. List Operations (Advanced)
| Command | Description |
| ------- | ----------- |
| `lindex <key> <index>` | Get an element from a list by its index |
| `linsert <key> BEFORE/AFTER <pivot> <value>` | Insert an element before or after another element |
| `lset <key> <index> <value>` | Set the value of an element in a list by index |
| `ltrim <key> <start> <stop>` | Trim a list to the specified range |
| `rpoplpush <source> <destination>` | Remove last element from source, add to destination |
| `blpop <key> [<key> ...] <timeout>` | Blocking left pop (wait for element) |
| `brpop <key> [<key> ...] <timeout>` | Blocking right pop (wait for element) |

## 17. Set Operations (Advanced)
| Command | Description |
| ------- | ----------- |
| `sunion <key1> <key2>` | Return the union of multiple sets |
| `sinter <key1> <key2>` | Return the intersection of multiple sets |
| `sdiff <key1> <key2>` | Return the difference between sets |
| `sunionstore <destination> <key1> <key2>` | Store union in a new set |
| `sinterstore <destination> <key1> <key2>` | Store intersection in a new set |
| `sdiffstore <destination> <key1> <key2>` | Store difference in a new set |
| `spop <key> [count]` | Remove and return random members from a set |
| `srandmember <key> [count]` | Get random members from a set without removing |
| `smove <source> <destination> <member>` | Move a member from one set to another |
| `sscan <key> <cursor>` | Incrementally iterate set elements |

## 18. Sorted Set Operations (Advanced)
| Command | Description |
| ------- | ----------- |
| `zincrby <key> <increment> <member>` | Increment the score of a member |
| `zcount <key> <min> <max>` | Count members in a score range |
| `zrank <key> <member>` | Determine the index of a member |
| `zrevrank <key> <member>` | Determine the index of a member (high to low) |
| `zrevrange <key> <start> <stop>` | Get range in reverse order |
| `zrevrangebyscore <key> <max> <min>` | Get range by score in reverse |
| `zremrangebyrank <key> <start> <stop>` | Remove all members in a rank range |
| `zremrangebyscore <key> <min> <max>` | Remove all members in a score range |
| `zunionstore <dest> <numkeys> <key> [<key> ...]` | Union multiple sorted sets |
| `zinterstore <dest> <numkeys> <key> [<key> ...]` | Intersect multiple sorted sets |
| `zscan <key> <cursor>` | Incrementally iterate sorted set elements |

## 19. HyperLogLog (Probabilistic Data Structure)
| Command | Description |
| ------- | ----------- |
| `pfadd <key> <element> [<element> ...]` | Add elements to a HyperLogLog |
| `pfcount <key> [<key> ...]` | Return the approximated cardinality |
| `pfmerge <destkey> <sourcekey> [<sourcekey> ...]` | Merge multiple HyperLogLogs |

## 20. Geospatial Commands
| Command | Description |
| ------- | ----------- |
| `geoadd <key> <longitude> <latitude> <member>` | Add geospatial items |
| `geodist <key> <member1> <member2> [unit]` | Get distance between two members |
| `geopos <key> <member> [<member> ...]` | Get positions (longitude, latitude) of members |
| `georadius <key> <long> <lat> <radius> <unit>` | Query members within radius |
| `georadiusbymember <key> <member> <radius> <unit>` | Query members within radius of a member |
| `geohash <key> <member> [<member> ...]` | Get geohash string of positions |

## 21. Stream Commands
| Command | Description |
| ------- | ----------- |
| `xadd <stream> * <field> <value>` | Append a new entry to a stream |
| `xlen <stream>` | Get the number of entries in a stream |
| `xrange <stream> <start> <end>` | Get a range of entries from a stream |
| `xread [COUNT count] STREAMS <stream> <id>` | Read data from streams |
| `xgroup create <stream> <group> <id>` | Create a consumer group |
| `xreadgroup GROUP <group> <consumer> STREAMS <stream> <id>` | Read from stream via consumer group |
| `xack <stream> <group> <id>` | Acknowledge a message |
| `xpending <stream> <group>` | Get pending messages info |
| `xtrim <stream> MAXLEN <count>` | Trim stream to specified length |

## 22. Cluster Commands
| Command | Description |
| ------- | ----------- |
| `cluster info` | Get cluster information |
| `cluster nodes` | Get cluster nodes information |
| `cluster meet <ip> <port>` | Connect to a cluster node |
| `cluster slots` | Get array of cluster slot to node mappings |
| `cluster keyslot <key>` | Get hash slot of a key |

## 23. Performance and Monitoring
| Command | Description |
| ------- | ----------- |
| `slowlog get [count]` | Get the slow queries log |
| `slowlog len` | Get the length of the slow log |
| `slowlog reset` | Clear the slow log |
| `monitor` | Monitor all commands processed by the server in real-time |
| `client list` | Get the list of client connections |
| `client kill <ip:port>` | Kill a specific client connection |
| `memory usage <key>` | Estimate memory usage of a key |
| `memory stats` | Get memory statistics |

## 24. Common Use Cases

### Caching Example
```redis
# Set a cache value with expiration
SETEX user:1000:profile 3600 '{"name":"John","email":"john@example.com"}'

# Get cached value
GET user:1000:profile

# Set if not exists (cache miss handling)
SETNX user:1000:lock 1
```

### Session Storage
```redis
# Store session data
HSET session:abc123 user_id 1000
HSET session:abc123 username "john_doe"
HSET session:abc123 last_activity 1234567890
EXPIRE session:abc123 1800

# Get session data
HGETALL session:abc123
```

### Rate Limiting
```redis
# Simple rate limiting (10 requests per minute)
INCR rate:limit:user:1000
EXPIRE rate:limit:user:1000 60
GET rate:limit:user:1000
```

### Leaderboard
```redis
# Add scores to leaderboard
ZADD leaderboard 100 player1
ZADD leaderboard 200 player2
ZADD leaderboard 150 player3

# Get top 10 players
ZREVRANGE leaderboard 0 9 WITHSCORES

# Get player rank
ZREVRANK leaderboard player1
```

### Real-time Analytics
```redis
# Count unique visitors using HyperLogLog
PFADD visitors:2024-01-27 user123
PFADD visitors:2024-01-27 user456
PFCOUNT visitors:2024-01-27
```
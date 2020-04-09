# Geo Distributed LRU

A new Geo Distributed LRU (Least Recently Used) cache with time expiration. The client currently finds its closest server by checking which server can be pinged with the least amount of time. However, an alternate solution is to use GeoIP, however ordering servers as per geo location is more of a tedious task. This can be taken up as an enhancement.

## LRU has the following code functionalities 

central_server

For the client to connect and receive all server details. When a server comes up, it connects to central server to add itself to the central data store.

server

Can be run in the corresponding geo locations, to bring up a server with lru cache.

lru_cache

It is the implementation of Least recently used cache operations. This code has to be placed along with each server.

client

connects to central_server, receives server list, then connects to the nearest server, and perform LRU Cache operations.

Pending to implement - real time data streaming between geo locations.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)